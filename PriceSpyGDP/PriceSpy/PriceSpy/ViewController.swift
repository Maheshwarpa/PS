//
//  ViewController.swift
//  PriceSpy
//
//  Created by Maheshwar Punyam Anand on 11/4/23.
//

import UIKit
import Lottie
import AnimatedGradientView
class ViewController: UIViewController {

    
    @IBOutlet weak var logoAnimationView: LottieAnimationView!
    var name=""
    var user=""
    var pss=""
    @IBOutlet weak var usernameTF: UITextField!
    
    @IBOutlet weak var resetBTN: UIButton!
    @IBOutlet weak var loginBTN: UIButton!
    @IBOutlet weak var passwordTF: UITextField!
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        playAnime()
        
        self.passwordTF.isEnabled=false
               self.loginBTN.isEnabled=false
                self.resetBTN.isEnabled=false
                
                
                guard let uname=usernameTF.text,!uname.isEmpty else{
                    return
                }
                if(uname.elementsEqual("admin")){
                    self.passwordTF.isEnabled=true
                    passAction(passwordTF)
                }
                
    }
    
    
    @IBAction func passAction(_ sender: UITextField) {
        
        if(sender.isEnabled){
                    guard let pass=self.passwordTF.text,!pass.isEmpty else{
                        return
                    }
            pss=pass
                    if(pass.elementsEqual("12345")&&(name.elementsEqual("admin"))){
                        self.loginBTN.isEnabled=true
                        
                    }
                }
    }
    
    @IBAction func userAction(_ sender: UITextField) {
        
        if(sender.isEnabled){
            //self.passwordTF.isEnabled=true
             self.resetBTN.isEnabled=true
            guard let uname=usernameTF.text,!uname.isEmpty else{
                return
            }
            name=uname
            user=uname
            if(uname.elementsEqual("admin")){
                self.passwordTF.isEnabled=true
            }
            
        }
    }
    func playAnime(){
        
        logoAnimationView.contentMode =  .scaleAspectFit
        logoAnimationView.loopMode = .loop
    
        
        logoAnimationView.animationSpeed=0.5
        logoAnimationView.play()
        
        
        
        let animatedGradient = AnimatedGradientView(frame: view.bounds)
        animatedGradient.direction = .up
        animatedGradient.animationValues = [(colors: ["#6496A2", "#29D954"], .up, .axial),
        (colors: ["#D154DE", "#31F264", "#A728EE"], .right, .axial),
        (colors: ["#003973", "#E5E5BE"], .down, .axial),
        (colors: ["#1E9600", "#FFF200", "#FF0000"], .left, .axial)]
        view.insertSubview(animatedGradient, at: 0)
    }
    
    
    @IBAction func login(_ sender: UIButton) {
        
        if(sender.tag==0){
            if(user.elementsEqual("admin")&&(pss.elementsEqual("12345"))){
                let alert=UIAlertController(title: "PriceSpy", message: "Welcome to the world of PriceSpy 🤩", preferredStyle:UIAlertController.Style.alert)
                alert.addAction(UIAlertAction(title: "OK", style: UIAlertAction.Style.default))
                self.present(alert,animated: true)
            }
            else{
                let alert=UIAlertController(title: "PriceSpy", message: "Please check your username/password ❌", preferredStyle:UIAlertController.Style.alert)
                alert.addAction(UIAlertAction(title: "OK", style: UIAlertAction.Style.default))
                self.present(alert,animated: true)
            }
        }
        
        
    }
    
    @IBAction func reset(_ sender: UIButton) {
        if(sender.tag==1){
            self.usernameTF.text=""
            self.passwordTF.text=""
            self.passwordTF.isEnabled=false
            self.resetBTN.isEnabled=false
            self.loginBTN.isEnabled=false
            //self.usernameTF.isEnabled=false
        }
    }
    
    

}

