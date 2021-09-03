## BUDDY Token

☑️

<img width="639" alt="BUDlogo2" src="https://user-images.githubusercontent.com/80833988/131942836-c5007890-2f20-4bce-98d7-c86a03fdf13b.png">



📌 For our  graduation project our team: Natalia Burrey, Jonah Leggett, Miguel Ortega and Samuel Yang - assumed a role of a Fintech professional and very exited to introduce a  blockchain-based solution for a real world problem


## Table of content 📔
- [I. PROJECT OVERVIEW](https://github.com/JonahLeggett/Buddy_Token#i-project-overview)
    - [An executive summary](https://github.com/JonahLeggett/Buddy_Token#an-executive-summary)
- [II. TECHNICAL REQUIREMENTS](https://github.com/JonahLeggett/Buddy_Token#ii-technical-requirements)
    - [Software Version Control](https://github.com/JonahLeggett/Buddy_Token#software-version-control)
    - [Data Collection and Preparation](https://github.com/JonahLeggett/Buddy_Token#data-collection-and-preparation)
    - [Development](https://github.com/JonahLeggett/Buddy_Token#development)
    - [Documentation](https://github.com/JonahLeggett/Buddy_Token#documentation)
- [How to install](https://github.com/JonahLeggett/Buddy_Token#how-to-install)
- [Our team](https://github.com/JonahLeggett/Buddy_Token#team)
- [Links](https://github.com/JonahLeggett/Buddy_Token#links)
- [Licence](https://github.com/JonahLeggett/Buddy_Token/blob/main/LICENSE)


## I. PROJECT OVERVIEW

## An executive summary

##### Identify the Problem:

In the 21st century we are finally witnessing the legalization of CANNABIS. America has led the charge to decriminalize medical and recreational use of marijuana.    

Cannabis is now legal in 19 states- but not on the federal level. This means that small business owners such as dispensaries, manufacturers, & vendors cannot legally have a bank account or credit line.

Cannabis customers must withdraw cash from their bank accounts to make a purchase.

Cannabis business owners have to operate solely with cash. 

This is a complex problem and has to be addressed on a federal level.

In the meantime we would like to introduce a FinTech solution:

BUDDY Token - Ethereum based cryptocurrency .

##### WHY CRYPTO?

We use the crypto to attract new type of customer, who is more engaged and spends more

Programmable money is a  transparent, secure  way to control the capital

Moreover Etherium is an investable asset- which grows over time, offers a hedge for inflation.



##### FINTECH solution 

<img width="462" alt="Screen Shot 2021-09-02 at 7 50 38 PM" src="https://user-images.githubusercontent.com/80833988/131943299-9f861fe8-f9e6-45d0-b0ba-91f90e971dad.png">


<img width="585" alt="Screen Shot 2021-09-02 at 7 52 29 PM" src="https://user-images.githubusercontent.com/80833988/131943465-56478aa6-1f2f-4413-88db-b46daba9cbda.png">


## II. TECHNICAL REQUIREMENTS 


### Software Version Control 


- Repository [BUDDY TOKEN](https://github.com/JonahLeggett/Buddy_Token.git) was created on a GitHub.

- Our team made sure files were frequently committed to repository. 

- Commit messages with appropriate level of detail included with each commit. 

- Repository organized, relevant information about the project files included. 

### Data Collection and Preparation

<img width="502" alt="Screen Shot 2021-09-02 at 7 54 57 PM" src="https://user-images.githubusercontent.com/80833988/131943655-e0063bde-0903-4f00-9e26-389c5ca33bab.png">



Remix IDE used to interact with Etherium blockchain, create and deploy smart contracts. Remix - Ethereum IDE is an open source web and desktop application. It fosters a fast development cycle and has a rich set of plugins with intuitive GUIs. Remix is used for the entire journey of contract development as well as being a playground for learning and teaching Ethereum.

OpenZeppelin provides security products to build, automate, and operate decentralized applications. We also protect leading organizations by performing security audits on their systems and products.

MetaMask allows users to store and manage account keys, broadcast transactions, send and receive Ethereum-based cryptocurrencies and tokens, and securely connect to decentralized applications through a compatible web browser or the mobile app's built-in browser. For the purpose of challange we will create an enviroment and use paper trade Etherium to showcase crowdsale of our Token

Ganache allows us to quickly fire up a personal Ethereum blockchain which you can use to run tests, execute commands, and inspect state while controlling how the chain operates. we will use it in this challenge to create a personal blockchain for rapid Ethereum distributed application development and test our crowdsale contract in a safe and deterministic environment.

IPFS The InterPlanetary File System is a protocol and peer-to-peer network for storing and sharing data in a distributed file system. IPFS uses content-addressing to uniquely identify each file in a global namespace connecting all computing devices.


### Development

- Streamlit application created. You can find a demonstration following link

https://www.youtube.com/watch?v=ltaTwjhq5u8


- 2 Solidity smart contracts created:

##### BuddyToken.sol (ERC-20)

<img width="1103" alt="Screen Shot 2021-09-02 at 8 11 44 PM" src="https://user-images.githubusercontent.com/80833988/131945139-7c7552da-785d-4cd6-a489-e88ce2b6cc4c.png">

 
##### BuddyNFT.sol (ERC-721)

<img width="963" alt="Screen Shot 2021-09-02 at 8 14 07 PM" src="https://user-images.githubusercontent.com/80833988/131945266-40e99ed4-d5aa-42f3-97e0-74e20e6b6b0e.png">


- Following video is demonstrating the application NFT contract for creating a coupon


https://user-images.githubusercontent.com/80833988/131944463-e379c6e8-929f-42d6-8285-eb19e970c375.mov

And this is the final version of an NFT coupon:

https://user-images.githubusercontent.com/80833988/131944536-44c37dc3-31fc-4037-9a7b-8c0b62449cb2.mp4

##### Libraries
We used following Open Zeppelin lib, some of them was not covered in the class

```

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Snapshot.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/draft-ERC20Permit.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Votes.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20FlashMint.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol"
```

#### Documentation 
* You can find Code written in Solidity, well commented with concise, relevant notes. 

* GitHub README.md file includes a concise project overview. We followed step by step [Technical requirements](https://courses.bootcampspot.com/courses/740/pages/23-dot-23-dot-5-technical-requirements?module_item_id=204832) for grading team convenience.

* GitHub README.md file includes detailed usage and installation instructions [How to install](https://github.com/JonahLeggett/Buddy_Token#how-to-install)
* GitHub README.md file includes examples of deployment, the application .

## How to install

##### Repository

* Save remote repo from GitHub to your computer (Desktop): 
in Terminal type:

```
cd desktop

git clone https://github.com/JonahLeggett/Buddy_Token.git
```

Now you can find repo on your desktop



## Team

<img width="371" alt="Screen Shot 2021-08-31 at 1 53 55 AM" src="https://user-images.githubusercontent.com/80833988/131473263-95a1f694-a1dd-4147-a5a7-a3fa49372d58.png">


📩 [Jonah Leggett](https://github.com/JonahLeggett) *☎️ +1(415) 430-8265 📧 Jonah.Leggett@gmail.com
📩 [Miguel Ortega](https://github.com/Miggs00) *☎️ +1(209) 417-7944 📧 mortega0014@gmail.com
📩 [Natalia Burrey](https://github.com/nataliaburrey) *☎️ +1(805)722-2619 📧 nataliaburrey@gmail.com
📩 [Samuel Yang](https://github.com/samjinyang) *☎️ +1(714) 609-8073 📧 Samueljinyang@gmail.com


## Links

* [Original Repository copy link](https://github.com/JonahLeggett/Buddy_Token.git)
* [Presentation Prezi Website](https://prezi.com/view/wWKYdjAMz2Ovw4d1IyZ3/)

## License

:star: MIT [LICENSE](https://github.com/JonahLeggett/Buddy_Token/blob/main/LICENSE)



