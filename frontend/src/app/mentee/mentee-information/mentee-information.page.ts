import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MenteeService } from '../shared/mentee.service';
import { Mentee } from '../shared/mentee.model';
import { LoaderService } from '../../shared/service/loader.service';
import { ToastService } from '../../shared/service/toast.service';

@Component({
  selector: 'app-mentee-information',
  templateUrl: './mentee-information.page.html',
  styleUrls: ['./mentee-information.page.scss']
})

export class MenteeInformationPage {

  menteeDeck: Mentee;
  menteeId: any;


  constructor(private route: ActivatedRoute,
              private menteeService: MenteeService) { 
    
    this.getMentees();
  }


   private getMentees() {
    this.menteeService.getAllmenteeDecks().subscribe(menteeDecks => {
         this.menteeDeck = menteeDecks.objects;
         this.menteeId = this.route.snapshot.paramMap.get('id');
        // this.FirstName = this.menteeDeck.first_name;
        // this.LastName = this.route.snapshot.paramMap.get('last_name');
        // this.City = this.route.snapshot.paramMap.get('city');
        // this.State = this.route.snapshot.paramMap.get('state');
     
      
    });
  }

}
