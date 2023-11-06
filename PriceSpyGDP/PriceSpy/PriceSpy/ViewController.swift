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
    @IBOutlet weak var usernameTF: UITextField!
    
    @IBOutlet weak var loginBTN: UIButton!
    @IBOutlet weak var passwordTF: UITextField!
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        playAnime()
        
        self.passwordTF.isEnabled=false
               self.loginBTN.isEnabled=false
                //self.resetBTN.isEnabled=false
                
                
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
                    if(pass.elementsEqual("12345")&&(name.elementsEqual("admin"))){
                        self.loginBTN.isEnabled=true
                        
                    }
                }
    }
    
    @IBAction func userAction(_ sender: UITextField) {
        
        if(sender.isEnabled){
            //self.passwordTF.isEnabled=true
            // self.resetBTN.isEnabled=true
            guard let uname=usernameTF.text,!uname.isEmpty else{
                return
            }
            name=uname
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
        animatedGradient.animationValues = [(colors: ["#2BC0E4", "#EAECC6"], .up, .axial),
        (colors: ["#833ab4", "#fd1d1d", "#fcb045"], .right, .axial),
        (colors: ["#003973", "#E5E5BE"], .down, .axial),
        (colors: ["#1E9600", "#FFF200", "#FF0000"], .left, .axial)]
        view.insertSubview(animatedGradient, at: 0)
    }


}

