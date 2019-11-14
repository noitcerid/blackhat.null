# blackhat.null
Blackhat.null (not entirely sure the name will stick) is inspired by the original "Uplink" game by Introversion. The goal of this game is really to 
provide a learning experience for pythonistas like myself to have a place to "hack" and build a usable and (hopefully)
interesting game. The intention isn't to build a full UX unless later time permits (or I find someone interested in 
contributing to the project).

If you haven't played the original Uplink game, I highly recommend it (it can be found on Steam) as even today it 
manages to hold it's own. Some of the data is slightly dated, but was also a fictitious world.

## Application Structure

### classes
This folder is (as the name implies) for the classes utilized in the application. Having these in a standard location
allows for a more organized structure and avoids cluttering the "main" application folder. 

### tests
Contains test classes, which should be grouped by class. Future testing around interactivity of classes will
likely be an additional task once that comes together more. 

## To Dos:

### Class expansion + development
There is a lot of remaining work to finish the core classes around the interactive elements of the game, but the 
initial elements should allow for the basic understanding of where I'm attempting to get to in the class.

Additional classes need to be added to allow for functionality like giving a "hacker" a way to be able to expand their
physical machine (Workstation) to speed up processing (Processor), data transfers (Network), Storage Capacity (Disk), 
and RAM (Memory) to provide additional speed/performance.

Networks could be another realm to provide an interface 
for breaking into.

### Application interface
The intention is to leave the application as a "console" to give it more of a basic feel and stick to more traditional 
command-line hacking techniques. I'm open to suggestions if anyone feels strongly or can provide UI enhancements to make
it a bit more friendly, but I overall enjoy the simplicity it offers (and who isn't nostalgic about seeing a blinking
underscore?)

### API
Longer term, it may make sense to give this a back-end API that could be then set to make remote calls and allow for
sharing of sites/instances of the game, or a more robust client/server experience.
