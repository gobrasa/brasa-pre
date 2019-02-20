import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MenteeService } from '../shared/mentee.service';
import { Mentee } from '../shared/mentee.model';
import { LoaderService } from '../../shared/service/loader.service';
import { ToastService } from '../../shared/service/toast.service';

@Component({
  selector: 'app-mentee-listing',
  templateUrl: './mentee-listing.page.html',
  styleUrls: ['./mentee-listing.page.scss']
})

export class MenteeListingPage {

  private readonly ALLOWED_DESCRIPTIONS = ["objects"];

  private menteeDecks: Mentee;

  constructor(private route: ActivatedRoute,
              private menteeService: MenteeService) {

    this.getMentees();
  }

   private getMentees() {
    this.menteeService.getAllmenteeDecks().subscribe(menteeDecks => {
        this.menteeDecks = menteeDecks;

    });
  }



}
