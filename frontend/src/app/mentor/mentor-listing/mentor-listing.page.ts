import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router'
import { MentorService } from '../shared/mentor.service';
import { Mentor } from '../shared/mentor.model'
import { LoaderService } from '../../shared/service/loader.service'
import { ToastService } from '../../shared/service/toast.service'

@Component({
  selector: 'app-mentor-listing',
  templateUrl: './mentor-listing.page.html',
  styleUrls: ['./mentor-listing.page.scss'],
})
export class MentorListingPage {

  mentorDeckGroup: string;
  mentorDeck: string;

  mentors: Mentor[] = [];
  copyOfMentors: Mentor[] = [];

  constructor(private route: ActivatedRoute,
  private mentorService: MentorService,
  private loaderService: LoaderService,
  private toaster: ToastService) { }


  private getMentors(){
  this.loaderService.presentLoading();
  /*
  this.mentorService.getMentorsByDeck(this.mentorDeckGroup, this.mentorDeck).subscribe(
    (mentors: Mentor[]) => {
      this.mentors = mentors.map((mentor: Mentor) => {
        mentor.text = this.mentorService.replaceMentorTextLine(mentor.text);
        return mentor;
      });

      this.copyOfMentors = Array.from(this.mentors);
      this.loaderService.dismissLoading();
    }, () => {
    this.loaderService.dismissLoading();
    this.toaster.presentErrorToast('mentor could not be loaded, try to refresh the page');
    })
  */
  }



    async ionViewWillEnter() {

      //this.mentorDeckGroup = this.route.snapshot.paramMap.get('mentorDeckGroup');
      //this.mentorDeck = this.route.snapshot.paramMap.get('mentorDeck');
      if (this.mentors && this.mentors.length === 0) this.getMentors();

    }

    doRefresh(event) {
      this.getMentors();
      event.target.complete();
    };

    hydrateMentors(mentors: Mentor[]){
      this.mentors = mentors;

    }



}
