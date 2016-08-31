A common question that I see in Desktop Support is “Why is ArcMap performing so slowly?” This can be a particularly tricky question as the answer depends on so many factors. For some, the answer is related to having a DEM with ½ centimeter accuracy turned on for the entire contiguous U.S., along with parcels, hydrology, streets network, and land use data for an entire county, with a 50% transparency set to each layer. Of course this example is an exaggeration, but it is true that we (myself included) expect our computers to handle whatever we throw at them and still get optimal performance. While the solution to the question can sometimes be to reduce the amount of layers ArcMap needs to draw, there can be times where the analyses that we are running are completely reasonable and the performance that we are experiencing is not. Here are several troubleshooting steps that resolve a lot of performance related issues that I see in Desktop Support.


Reboot your machine. I, too, am a victim of leaving my machine on for days on end. This can cause applications and processes to pile up in the Task Manager and, because of this, we can expect slow performance. It is best to start with a clean slate and reboot the machine.
Do you meet the minimum requirements? Some users upgrade from version 9.3 to version 10 without checking this, and later realize they don’t meet the RAM or video card requirements. The ”Can you run it utility” will scan your machine and tell you if it’s up to the task.
Is the behavior MXD specific? If you are experiencing unexpected behavior, the issue may be related to the MXD. To test this, open another instance of ArcMap next to your existing MXD and drag and drop your layers into the new MXD. Test to see if the behavior persists. You can also try using the MXD Doctor. This will analyze your MXD for corrupt objects and will generate a new copy of your MXD. You can find this at Start > All Programs > ArcGIS > Desktop Utilities > MXD Doctor.
Is the behavior data specific? Similar to MXD issues, performance issues can be related to shapefiles, feature classes, or other data. Test to see if the issues persist with other datasets. If they do not, it may be data specific. Try exporting your feature classes out to a new location and test your workflow on this copy of the data.
Does this happen on other machines? While this suggestion won’t actually resolve any issues, it is helpful in narrowing down the problem. If everyone in your organization is having issues, it is most likely data, MXD, or network specific issues. If you are the only one, you know it is something with your configuration.
Does this happen if you log into the machine with a different Windows User Profile? This sounds bizarre, but ArcGIS for Desktop relies heavily on your Windows User Profile, so once in a while, these can become corrupt and you may need to consider creating a new profile.
Does this happen with local data? If you are working with shapefiles or file/personal geodatabases on your network, try exporting them to your C drive. If the issues leave, it may very well be a network issue. In this case, you will want to talk with IT to discuss potential causes and solutions. If you are using SDE data and you export to a local file geodatabase and it resolves the issue, you will want to look into your SDE connection.
Rename your Normal templates.The normal template is the template that is automatically loaded from your user profile every time you launch ArcGIS for Desktop. It contains the UI customizations you have made, including toolbars, buttons, window placements, and more. These templates can become corrupt, so by renaming them, you will prompt the software to generate a new, default normal template. Here is how to rename your normal template in version 10:
Close ArcCatalog and ArcMap.
Navigate to root %userprofile%\AppData*\Roaming\ESRI\Desktop10.0\ArcMap (*if hidden go to the Tools folder options view).
Open the Templates folder.
There will be a “Normal.mxt” file. Right-click on that file, and rename it to something besides Normal. Then re-start ArcMap.
ArcCatalog and ArcToolbox also have normal templates. If need be, navigate to their respective folders and rename their normal templates as well.
Are you up to date on Service Packs? You can find an updated list of service packs and patches on our Resource Center.
Is your My Documents folder stored to your C drive? Some organizations map out their My Documents folders to their network. This can be problematic with ArcGIS for Desktop 10.x, as several files and folders that ArcMap relies on are stored here, including the Default.gdb. Talk with IT to see if you can get your My Documents folder redirected to your local drive.
Check for any 3rd party tools. There are a lot of great third party extensions out there, but unfortunately, we do not test or certify against them. Some can occasionally cause conflicts, so it is worth uninstalling these to see if the behavior persists. If it does, you may want to consider logging a support request with that third party company to see if it is a known issue. Here are a few places to check for hidden 3rdparty tools on your machine:
All programs and features in the Control Panel.
Look through the list of all toolbars in ArcMap (Open ArcMap > Customize > Toolbars)
Look through the list of all extensions in ArcMap (Open ArcMap > Customize > Extensions)
Look in the Add-In Manager (Open ArcMap > Customize > Add-in Manager)
Are you using continual scan anti-virus? Try temporarily disabling a continual scan anti-virus, as this can cause performance issues in ArcGIS for Desktop.
Do you have any drivers that need updating?
Open Control Panel > Device Manager.
Expand Display Adapters.
Right click the adapter below this > Properties.
Go to the Driver tab > Update Driver > Search Automatically.
If you can upgrade, then install the newer driver.
Redirect your temporary folders and optimize your Virtual Memory:
Navigate to Start > Settings > Control Panel > System (Advanced System Settings) > Advanced tab > Environment Variables.
For both TEMP and TMP, you will likely see a value such as C:/Users/<username>/AppData/Local/Temp.
If so, edit each so that they equal “C:/Temp”, without the quotes.
Click OK to close the Environment Variables window.
Under performance, click Settings.
Click Advanced.
For Virtual Memory, select Change.
Select System managed size > OK.
Again, keep in mind that there are limits on what we can realistically expect the software to do. If the above steps don’t resolve your performance issues, you may want to consider logging a request with Support Services and we’d be more than happy to continue testing from there.

- See more at: https://blogs.esri.com/esri/supportcenter/2012/06/07/troubleshooting-slow-performance-in-arcgis-desktop/#sthash.59abE1t3.dpuf