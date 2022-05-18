// A simple JS program to demonstrate
// implementation of Command Pattern using
// A SmartHouse as a example
   
// holds the inforamtion about a action and binds it to the reciver by inviking the operation on it
class Command {
    execute() {};
  }

  //TurnOnLignts command
  class TurnOnLights extends Command {
      
      constructor(house) {
          super();
          this.house = house;
          this.commandName = "turn on Lights" 
      }
      
      execute() {
          this.house.turnOnLights();
      }
  }
  
  //TurnOffLights command
  class TurnOffLights extends Command {
  
    constructor(house) {
      super();
      this.house = house;
      this.commandName = "turn off Lights" 
    }
    
    execute() {
      this.house.turnOffLights();
    }
    
  }
  
  //Lock command
  class LockDoor extends Command {
  
    constructor(house) {
      super();
      this.house = house;
      this.commandName = "Locking Doors" 
    }
    
    execute() {
      this.house.lockDoor();
    }
    
  }
  
  //Invoker
  class HouseInvoker {
      pressButton(command) {
          console.log(`${command.commandName} `);
          command.execute();
      }
  }
  
  //Reciever: 
  class House {
  
    turnOnLights() {
      console.log('Lights On');
    }
    
    turnOffLights() {
      console.log('Lights Off');
    }
  
    lockDoor(){
        console.log('Door Locked')
    }
  }
  
  
  const house = new House();
  const turnOnCommand = new TurnOnLights(house);
  const turnOffCommand = new TurnOffLights(house);
  const lockCommand = new LockDoor(house);

  
  const invoker = new HouseInvoker();
  invoker.pressButton(turnOnCommand);
  invoker.pressButton(turnOffCommand);
  invoker.pressButton(lockCommand);
  
console.log(`invoker isHouseInvoker: ${invoker instanceof HouseInvoker}`);
console.log(`turnOnCommand is TurnOnLights: ${turnOnCommand instanceof TurnOnLights}`);
console.log(`turnOffCommand is TurnOffLights: ${turnOffCommand instanceof TurnOffLights}`);
console.log(`lockCommand is LockDoor: ${lockCommand instanceof LockDoor}`);


