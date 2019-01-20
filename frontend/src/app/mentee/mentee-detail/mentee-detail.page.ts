import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router'
import { MenteeService } from '../shared/mentee.service';
import { Mentee } from '../shared/mentee.model'
import { LoaderService } from '../../shared/service/loader.service'
import { AlertService } from '../../shared/service/alert.service'


@Component({
  selector: 'app-mentee-detail',
  templateUrl: './mentee-detail.page.html',
  styleUrls:  ['./mentee-detail.page.scss']
})
export class MenteeDetailPage {

  mentee: Mentee;

  constructor(private route: ActivatedRoute,
              private menteeService: MenteeService,
              private loaderService: LoaderService,
              private alertSerice: AlertService) { }

  ionViewWillEnter() {
    const menteeId = this.route.snapshot.paramMap.get('menteeId');

    this.loaderService.presentLoading();
    this.menteeService.getMenteeById(menteeId).subscribe(
      (mentee: Mentee[]) => {
        /*
        this.mentee = mentee.map((mentee: Mentee) => {
          mentee.text = this.menteeService.replaceMenteeTextLine(mentee.text);

          return mentee;
        })[0];
        */

        this.loaderService.dismissLoading();
    });
  }

  updateImage() {
    /*
    this.mentee.img = 'assets/image/DefaultMentee.png'
    */
  }

}
