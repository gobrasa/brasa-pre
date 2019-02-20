import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MentorService } from '../shared/mentor.service';
import { Mentor } from '../shared/mentor.model';
import { LoaderService } from '../../shared/service/loader.service';
import { ToastService } from '../../shared/service/toast.service';

@Component({
  selector: 'app-mentor-information',
  templateUrl: './mentor-information.page.html'
})

export class MentorInformationPage {

  private mentorDeck: Mentor;
  private mentorDeckCycle: Mentor;
  mentorId: any;


  constructor(private route: ActivatedRoute,
              private mentorService: MentorService) { 
    
    this.getMentors();
  }


   private getMentors() {
    this.mentorService.getAllmentorsDecks().subscribe(mentorDecks => {
         this.mentorDeck = mentorDecks;
         this.mentorId = this.route.snapshot.paramMap.get('id');
     
          console.log(this.mentorDeck);
    });
  }

}