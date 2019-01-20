import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router'
import { MenteeService } from '../shared/mentee.service';
import { Mentee } from '../shared/mentee.model'
import { LoaderService } from '../../shared/service/loader.service'
import { ToastService } from '../../shared/service/toast.service'

@Component({
  selector: 'app-mentee-listing',
  templateUrl: './mentee-listing.page.html',
  styleUrls: ['./mentee-listing.page.scss'],
})
export class MenteeListingPage {

  menteeDeckGroup: string;
  menteeDeck: string;

  mentees: Mentee[] = [];
  copyOfMentees: Mentee[] = [];

  constructor(private route: ActivatedRoute,
  private menteeService: MenteeService,
  private loaderService: LoaderService,
  private toaster: ToastService) { }


  private getMentees(){
  this.loaderService.presentLoading();
  /*
  this.menteeService.getMenteesByDeck(this.menteeDeckGroup, this.menteeDeck).subscribe(
    (mentees: Mentee[]) => {
      this.mentees = mentees.map((mentee: Mentee) => {
        mentee.text = this.menteeService.replaceMenteeTextLine(mentee.text);
        return mentee;
      });

      this.copyOfMentees = Array.from(this.mentees);
      this.loaderService.dismissLoading();
    }, () => {
    this.loaderService.dismissLoading();
    this.toaster.presentErrorToast('mentee could not be loaded, try to refresh the page');
    })
  */
  }



    async ionViewWillEnter() {

      //this.menteeDeckGroup = this.route.snapshot.paramMap.get('menteeDeckGroup');
      //this.menteeDeck = this.route.snapshot.paramMap.get('menteeDeck');
      if (this.mentees && this.mentees.length === 0) this.getMentees();

    }

    doRefresh(event) {
      this.getMentees();
      event.target.complete();
    };

    hydrateMentees(mentees: Mentee[]){
      this.mentees = mentees;

    }



}
