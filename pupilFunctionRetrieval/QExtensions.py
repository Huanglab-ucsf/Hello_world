#!/usr/bin/python

import numpy as np
from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import QWidget,QImage
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import sc_library.hdebug as hdebug

def bind(objectName, propertyName, type):
    _child = self.findChild(QtCore.QObject, objectName)
    def getter(self):
        _pyObject = _child.property(propertyName).toPyObject()
        return type(_pyObject)
    def setter(self, value):
        _child.setProperty(propertyName, QtCore.QVariant(value))    
    return property(getter, setter)



class ProgressDialog(QtGui.QProgressDialog):
        def __init__(self,message,min_,max_):
                QtGui.QProgressDialog.__init__(self,message,
                                               'Cancel',
                                               min_,
                                               max_)
                self.setWindowModality(QtCore.Qt.WindowModal)
                self.setWindowTitle('Please wait')
                self.setValue(min_)

def saveWithDialog(title,filters,data):
        fname = QtGui.QFileDialog.getSaveFileName(None,title,'',filters)
        if fname:
                np.save(str(fname),data)

@hdebug.debug
def numpy_to_qimage8(array,vmin=0,vmax=65535,cmap=None,color=False,c='r'):
        image = np.ndarray.copy(array)
        
        # Clip:
        image[image<vmin] = vmin
        image[image>vmax] = vmax

        # Scale within clip interval:
        image -= vmin
        if vmax != 0.0:
                image *= 255.0/(vmax-vmin)

        # Convert to 8-bit data:
        image = np.uint8(np.round(image))

        nx,ny = image.shape

        if color:
            cimage = np.zeros((nx,ny,3),np.uint8,'C')
            if c=='r':
                cimage[:,:,0] = image
            elif c=='g':
                cimage[:,:,1] = image
            elif c=='b':
                cimage[:,:,2] = image
            elif c=='y':
                cimage[:,:,0] = image
                cimage[:,:,1] = image
            elif c=='c':
                cimage[:,:,1] = image
                cimage[:,:,2] = image
            #image = np.copy(cimage)
            useFormat = QImage.Format_RGB888
            qt_image = QImage(cimage.data,nx,ny,useFormat)
            qt_image.ndarray = cimage
            return qt_image
        else:
            useFormat = QImage.Format_Indexed8

      
        qt_image = QImage(image.data,nx,ny,useFormat)
        qt_image.ndarray = image
        if cmap != None:
            qt_image.setColorTable(cmap)

        return qt_image

@hdebug.debug
def numpy_to_qimage8_dual(array1,array2,vmin=0,vmax=65535,cmap=None,c1='r',c2='g'):
        image1 = np.copy(array1)
        
        # Clip:
        image1[image1<vmin] = vmin
        image1[image1>vmax] = vmax

        # Scale within clip interval:
        image1 -= vmin
        if vmax != 0.0:
                image1 *= 255.0/(vmax-vmin)

        # Convert to 8-bit data:
        image1 = np.uint8(np.round(image1))

        image2 = np.copy(array2)
        
        # Clip:
        image2[image2<vmin] = vmin
        image2[image2>vmax] = vmax

        # Scale within clip interval:
        image2 -= vmin
        if vmax != 0.0:
                image2 *= 255.0/(vmax-vmin)

        # Convert to 8-bit data:
        image2 = np.uint8(np.round(image2))

        nx,ny = image1.shape

        if 1:
            cimage = np.zeros((nx,ny,3),np.uint8,'C')
            if c1=='r':
                cimage[:,:,0] = image1
            elif c1=='g':
                cimage[:,:,1] = image1
            elif c1=='b':
                cimage[:,:,2] = image1
            elif c1=='y':
                cimage[:,:,0] = image1
                cimage[:,:,1] = image1
            elif c1=='c':
                cimage[:,:,1] = image1
                cimage[:,:,2] = image1
            if c2=='r':
                cimage[:,:,0] = image2
            elif c2=='g':
                cimage[:,:,1] = image2
            elif c2=='b':
                cimage[:,:,2] = image2
            elif c2=='y':
                cimage[:,:,0] = image2
                cimage[:,:,1] = image2
            elif c2=='c':
                cimage[:,:,1] = image2
                cimage[:,:,2] = image2
            #image = cimage
            useFormat = QImage.Format_RGB888


      
        qt_image = QImage(cimage.data,nx,ny,useFormat)
        qt_image.ndarray = cimage
        if cmap != None:
            qt_image.setColorTable(cmap)

        return qt_image


class QMatplotlibCanvas(FigureCanvas):
        def __init__(self):
                self.figure = Figure()
                self.axes = self.figure.add_subplot(111)
                FigureCanvas.__init__(self,self.figure)


class QColortables8:
        RdBu = [4284940319L,
                 4285137183L,
                 4285334048L,
                 4285530912L,
                 4285727777L,
                 4285924641L,
                 4286121506L,
                 4286318370L,
                 4286515235L,
                 4286646307L,
                 4286843172L,
                 4287040036L,
                 4287236901L,
                 4287433765L,
                 4287630630L,
                 4287827494L,
                 4288024359L,
                 4288221223L,
                 4288418087L,
                 4288614952L,
                 4288811816L,
                 4289008681L,
                 4289205545L,
                 4289402410L,
                 4289599274L,
                 4289796139L,
                 4289927468L,
                 4289993773L,
                 4290125614L,
                 4290191920L,
                 4290258225L,
                 4290390066L,
                 4290456116L,
                 4290587957L,
                 4290654262L,
                 4290720568L,
                 4290852409L,
                 4290918458L,
                 4291050300L,
                 4291116605L,
                 4291182910L,
                 4291314752L,
                 4291381057L,
                 4291512642L,
                 4291578948L,
                 4291710789L,
                 4291777094L,
                 4291843400L,
                 4291975241L,
                 4292041290L,
                 4292173132L,
                 4292239437L,
                 4292305743L,
                 4292371793L,
                 4292503635L,
                 4292569941L,
                 4292636247L,
                 4292702297L,
                 4292768604L,
                 4292834910L,
                 4292966496L,
                 4293032802L,
                 4293099108L,
                 4293165158L,
                 4293231464L,
                 4293297770L,
                 4293429612L,
                 4293495662L,
                 4293561968L,
                 4293628274L,
                 4293694324L,
                 4293826167L,
                 4293892473L,
                 4293958779L,
                 4294024829L,
                 4294091135L,
                 4294157441L,
                 4294223491L,
                 4294289542L,
                 4294290057L,
                 4294290571L,
                 4294356878L,
                 4294357393L,
                 4294357908L,
                 4294423958L,
                 4294424473L,
                 4294424988L,
                 4294491038L,
                 4294491553L,
                 4294492068L,
                 4294558375L,
                 4294558889L,
                 4294559404L,
                 4294625455L,
                 4294625969L,
                 4294692020L,
                 4294692535L,
                 4294693049L,
                 4294759356L,
                 4294759871L,
                 4294760386L,
                 4294826436L,
                 4294826951L,
                 4294827209L,
                 4294827467L,
                 4294762189L,
                 4294762447L,
                 4294762704L,
                 4294763218L,
                 4294697940L,
                 4294698198L,
                 4294698456L,
                 4294698714L,
                 4294633436L,
                 4294633694L,
                 4294633951L,
                 4294634209L,
                 4294568931L,
                 4294569445L,
                 4294569703L,
                 4294569961L,
                 4294570219L,
                 4294504941L,
                 4294505199L,
                 4294505456L,
                 4294505714L,
                 4294440436L,
                 4294440694L,
                 4294375415L,
                 4294309623L,
                 4294178294L,
                 4294112758L,
                 4293981430L,
                 4293915637L,
                 4293784309L,
                 4293718773L,
                 4293587445L,
                 4293521652L,
                 4293390580L,
                 4293324788L,
                 4293193460L,
                 4293127667L,
                 4292996595L,
                 4292930803L,
                 4292799474L,
                 4292733938L,
                 4292602610L,
                 4292536818L,
                 4292405745L,
                 4292339953L,
                 4292208625L,
                 4292142833L,
                 4292011760L,
                 4291945968L,
                 4291814639L,
                 4291617519L,
                 4291486190L,
                 4291289325L,
                 4291157996L,
                 4290960876L,
                 4290829547L,
                 4290632682L,
                 4290501354L,
                 4290304233L,
                 4290172904L,
                 4289976040L,
                 4289844711L,
                 4289647590L,
                 4289516261L,
                 4289319397L,
                 4289188068L,
                 4289056483L,
                 4288859619L,
                 4288728290L,
                 4288531425L,
                 4288399840L,
                 4288202976L,
                 4288071647L,
                 4287874782L,
                 4287677661L,
                 4287480540L,
                 4287283419L,
                 4287086298L,
                 4286889177L,
                 4286692056L,
                 4286494935L,
                 4286297814L,
                 4286100693L,
                 4285903572L,
                 4285640915L,
                 4285443794L,
                 4285246673L,
                 4285049808L,
                 4284852687L,
                 4284655566L,
                 4284458445L,
                 4284261323L,
                 4284064202L,
                 4283867081L,
                 4283604424L,
                 4283407303L,
                 4283210182L,
                 4283013061L,
                 4282815940L,
                 4282618819L,
                 4282552770L,
                 4282421185L,
                 4282355392L,
                 4282289343L,
                 4282157758L,
                 4282091710L,
                 4282025917L,
                 4281894332L,
                 4281828283L,
                 4281762234L,
                 4281630905L,
                 4281564856L,
                 4281498807L,
                 4281367222L,
                 4281301429L,
                 4281235381L,
                 4281103796L,
                 4281037747L,
                 4280971698L,
                 4280840369L,
                 4280774320L,
                 4280708271L,
                 4280576686L,
                 4280510893L,
                 4280444844L,
                 4280313259L,
                 4280247208L,
                 4280181157L,
                 4280115106L,
                 4280048799L,
                 4279982748L,
                 4279916697L,
                 4279850646L,
                 4279784595L,
                 4279718544L,
                 4279586957L,
                 4279520906L,
                 4279454855L,
                 4279388548L,
                 4279322497L,
                 4279256446L,
                 4279190395L,
                 4279124345L,
                 4279058294L,
                 4278992243L,
                 4278860656L,
                 4278794349L,
                 4278728298L,
                 4278662247L,
                 4278596196L,
                 4278530145L]
        spectral = [4278190080L,
                 4278779915L,
                 4279435285L,
                 4280025120L,
                 4280614955L,
                 4281270325L,
                 4281860160L,
                 4282449995L,
                 4283105365L,
                 4283695200L,
                 4284285035L,
                 4284940405L,
                 4285530240L,
                 4285989000L,
                 4286120074L,
                 4286185611L,
                 4286251148L,
                 4286382222L,
                 4286447759L,
                 4286513296L,
                 4286644370L,
                 4286709907L,
                 4286775444L,
                 4286906518L,
                 4286972055L,
                 4287037592L,
                 4286775450L,
                 4286054555L,
                 4285333660L,
                 4284678302L,
                 4283957407L,
                 4283236512L,
                 4282581154L,
                 4281860259L,
                 4281139364L,
                 4280484006L,
                 4279763111L,
                 4279042216L,
                 4278386858L,
                 4278190253L,
                 4278190257L,
                 4278190261L,
                 4278190265L,
                 4278190269L,
                 4278190273L,
                 4278190277L,
                 4278190281L,
                 4278190285L,
                 4278190289L,
                 4278190293L,
                 4278190297L,
                 4278190301L,
                 4278192605L,
                 4278195165L,
                 4278197469L,
                 4278199773L,
                 4278202333L,
                 4278204637L,
                 4278206941L,
                 4278209501L,
                 4278211805L,
                 4278214109L,
                 4278216669L,
                 4278218973L,
                 4278221021L,
                 4278221533L,
                 4278222301L,
                 4278223069L,
                 4278223581L,
                 4278224349L,
                 4278225117L,
                 4278225629L,
                 4278226397L,
                 4278227165L,
                 4278227677L,
                 4278228445L,
                 4278229213L,
                 4278229723L,
                 4278229975L,
                 4278230227L,
                 4278230735L,
                 4278230987L,
                 4278231239L,
                 4278231747L,
                 4278231999L,
                 4278232251L,
                 4278232759L,
                 4278233011L,
                 4278233263L,
                 4278233771L,
                 4278233768L,
                 4278233765L,
                 4278233763L,
                 4278233760L,
                 4278233757L,
                 4278233755L,
                 4278233752L,
                 4278233749L,
                 4278233747L,
                 4278233744L,
                 4278233741L,
                 4278233739L,
                 4278233736L,
                 4278233469L,
                 4278232947L,
                 4278232680L,
                 4278232413L,
                 4278231891L,
                 4278231624L,
                 4278231357L,
                 4278230835L,
                 4278230568L,
                 4278230301L,
                 4278229779L,
                 4278229512L,
                 4278229504L,
                 4278230016L,
                 4278230784L,
                 4278231552L,
                 4278232064L,
                 4278232832L,
                 4278233600L,
                 4278234112L,
                 4278234880L,
                 4278235648L,
                 4278236160L,
                 4278236928L,
                 4278237696L,
                 4278238208L,
                 4278238976L,
                 4278239744L,
                 4278240256L,
                 4278241024L,
                 4278241792L,
                 4278242304L,
                 4278243072L,
                 4278243840L,
                 4278244352L,
                 4278245120L,
                 4278245888L,
                 4278246400L,
                 4278247168L,
                 4278247936L,
                 4278248448L,
                 4278249216L,
                 4278249984L,
                 4278250496L,
                 4278251264L,
                 4278252032L,
                 4278252544L,
                 4278253312L,
                 4278254080L,
                 4278254592L,
                 4278255360L,
                 4279238400L,
                 4280155904L,
                 4281138944L,
                 4282121984L,
                 4283039488L,
                 4284022528L,
                 4285005568L,
                 4285923072L,
                 4286906112L,
                 4287889152L,
                 4288806656L,
                 4289789696L,
                 4290576128L,
                 4290837760L,
                 4291099648L,
                 4291361536L,
                 4291623168L,
                 4291885056L,
                 4292146944L,
                 4292408576L,
                 4292670464L,
                 4292932352L,
                 4293193984L,
                 4293455872L,
                 4293717760L,
                 4293913856L,
                 4293978624L,
                 4294043392L,
                 4294173952L,
                 4294238720L,
                 4294303488L,
                 4294434048L,
                 4294498816L,
                 4294563584L,
                 4294694144L,
                 4294758912L,
                 4294823680L,
                 4294954240L,
                 4294953216L,
                 4294952192L,
                 4294951168L,
                 4294950144L,
                 4294949120L,
                 4294948096L,
                 4294947072L,
                 4294946048L,
                 4294945024L,
                 4294944000L,
                 4294942976L,
                 4294941952L,
                 4294940928L,
                 4294937856L,
                 4294934784L,
                 4294931712L,
                 4294928640L,
                 4294925568L,
                 4294922496L,
                 4294919424L,
                 4294916352L,
                 4294913280L,
                 4294910208L,
                 4294907136L,
                 4294904064L,
                 4294836224L,
                 4294705152L,
                 4294508544L,
                 4294311936L,
                 4294180864L,
                 4293984256L,
                 4293787648L,
                 4293656576L,
                 4293459968L,
                 4293263360L,
                 4293132288L,
                 4292935680L,
                 4292739072L,
                 4292608000L,
                 4292542464L,
                 4292476928L,
                 4292345856L,
                 4292280320L,
                 4292214784L,
                 4292083712L,
                 4292018176L,
                 4291952640L,
                 4291821568L,
                 4291756032L,
                 4291690496L,
                 4291559424L,
                 4291562508L,
                 4291566620L,
                 4291570732L,
                 4291574844L,
                 4291578956L,
                 4291583068L,
                 4291587180L,
                 4291591292L,
                 4291595404L,
                 4291599516L,
                 4291603628L,
                 4291607740L,
                 4291611852L]

        gray = [4278190080L,
             4278255873L,
             4278321666L,
             4278387459L,
             4278453252L,
             4278519045L,
             4278584838L,
             4278650631L,
             4278716424L,
             4278782217L,
             4278848010L,
             4278913803L,
             4278979596L,
             4279045389L,
             4279111182L,
             4279176975L,
             4279242768L,
             4279308561L,
             4279374354L,
             4279440147L,
             4279505940L,
             4279571733L,
             4279637526L,
             4279703319L,
             4279769112L,
             4279834905L,
             4279900698L,
             4279966491L,
             4280032284L,
             4280098077L,
             4280163870L,
             4280229663L,
             4280295456L,
             4280361249L,
             4280427042L,
             4280492835L,
             4280558628L,
             4280624421L,
             4280690214L,
             4280756007L,
             4280821800L,
             4280887593L,
             4280953386L,
             4281019179L,
             4281084972L,
             4281150765L,
             4281216558L,
             4281282351L,
             4281348144L,
             4281413937L,
             4281479730L,
             4281545523L,
             4281611316L,
             4281677109L,
             4281742902L,
             4281808695L,
             4281874488L,
             4281940281L,
             4282006074L,
             4282071867L,
             4282137660L,
             4282203453L,
             4282269246L,
             4282335039L,
             4282400832L,
             4282466625L,
             4282532418L,
             4282598211L,
             4282664004L,
             4282729797L,
             4282795590L,
             4282861383L,
             4282927176L,
             4282992969L,
             4283058762L,
             4283124555L,
             4283190348L,
             4283256141L,
             4283321934L,
             4283387727L,
             4283453520L,
             4283519313L,
             4283585106L,
             4283650899L,
             4283716692L,
             4283782485L,
             4283848278L,
             4283914071L,
             4283979864L,
             4284045657L,
             4284111450L,
             4284177243L,
             4284243036L,
             4284308829L,
             4284374622L,
             4284440415L,
             4284506208L,
             4284572001L,
             4284637794L,
             4284703587L,
             4284769380L,
             4284835173L,
             4284900966L,
             4284966759L,
             4285032552L,
             4285098345L,
             4285164138L,
             4285229931L,
             4285295724L,
             4285361517L,
             4285427310L,
             4285493103L,
             4285558896L,
             4285624689L,
             4285690482L,
             4285756275L,
             4285822068L,
             4285887861L,
             4285953654L,
             4286019447L,
             4286085240L,
             4286151033L,
             4286216826L,
             4286282619L,
             4286348412L,
             4286414205L,
             4286479998L,
             4286545791L,
             4286611584L,
             4286677377L,
             4286743170L,
             4286808963L,
             4286874756L,
             4286940549L,
             4287006342L,
             4287072135L,
             4287137928L,
             4287203721L,
             4287269514L,
             4287335307L,
             4287401100L,
             4287466893L,
             4287532686L,
             4287598479L,
             4287664272L,
             4287730065L,
             4287795858L,
             4287861651L,
             4287927444L,
             4287993237L,
             4288059030L,
             4288124823L,
             4288190616L,
             4288256409L,
             4288322202L,
             4288387995L,
             4288453788L,
             4288519581L,
             4288585374L,
             4288651167L,
             4288716960L,
             4288782753L,
             4288848546L,
             4288914339L,
             4288980132L,
             4289045925L,
             4289111718L,
             4289177511L,
             4289243304L,
             4289309097L,
             4289374890L,
             4289440683L,
             4289506476L,
             4289572269L,
             4289638062L,
             4289703855L,
             4289769648L,
             4289835441L,
             4289901234L,
             4289967027L,
             4290032820L,
             4290098613L,
             4290164406L,
             4290230199L,
             4290295992L,
             4290361785L,
             4290427578L,
             4290493371L,
             4290559164L,
             4290624957L,
             4290690750L,
             4290756543L,
             4290822336L,
             4290888129L,
             4290953922L,
             4291019715L,
             4291085508L,
             4291151301L,
             4291217094L,
             4291282887L,
             4291348680L,
             4291414473L,
             4291480266L,
             4291546059L,
             4291611852L,
             4291677645L,
             4291743438L,
             4291809231L,
             4291875024L,
             4291940817L,
             4292006610L,
             4292072403L,
             4292138196L,
             4292203989L,
             4292269782L,
             4292335575L,
             4292401368L,
             4292467161L,
             4292532954L,
             4292598747L,
             4292664540L,
             4292730333L,
             4292796126L,
             4292861919L,
             4292927712L,
             4292993505L,
             4293059298L,
             4293125091L,
             4293190884L,
             4293256677L,
             4293322470L,
             4293388263L,
             4293454056L,
             4293519849L,
             4293585642L,
             4293651435L,
             4293717228L,
             4293783021L,
             4293848814L,
             4293914607L,
             4293980400L,
             4294046193L,
             4294111986L,
             4294177779L,
             4294243572L,
             4294309365L,
             4294375158L,
             4294440951L,
             4294506744L,
             4294572537L,
             4294638330L,
             4294704123L,
             4294769916L,
             4294835709L,
             4294901502L,
             4294967295L]
