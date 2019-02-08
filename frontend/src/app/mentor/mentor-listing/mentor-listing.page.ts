import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MentorService } from '../shared/mentor.service';
import { Mentor } from '../shared/mentor.model';
import { LoaderService } from '../../shared/service/loader.service';
import { ToastService } from '../../shared/service/toast.service';

@Component({
  selector: 'app-mentor-listing',
  templateUrl: './mentor-listing.page.html',
  styleUrls: ['./mentor-listing.page.scss']
})

export class MentorListingPage {

  private readonly ALLOWED_DESCRIPTIONS = ["objects"];

  private mentorDecks: Mentor;

  constructor(private route: ActivatedRoute,
              private mentorService: MentorService) { 
    
    this.getMentors();
  }
  
   private getMentors() {
    this.mentorService.getAllmentorsDecks().subscribe(mentorDecks => {
        this.mentorDecks = mentorDecks;
      
    });
  }

  
  
}
