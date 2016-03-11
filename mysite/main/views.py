import os

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from django.template.loader import get_template
from django.template import Context

from mysite.news.models import News
from mysite.team.models import Team
from mysite.main.models import Pages
from mysite.jobs.models import Section
from mysite.ambassadors.models import Ambassadors
from mysite.settings import GOOGLE_APPLICATION_REDIRECT_URI, GOOGLE_REDIRECT_SESSION_VAR
from mysite.forms import ContactForm

class AboutPageView(generic.TemplateView):
    template_name = 'page/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'about')
        return context


class AboutBoardPageView(generic.TemplateView):
    template_name = 'page/about_board.html'

    def get_context_data(self, **kwargs):
        context = super(AboutBoardPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'about_board')
        return context


class ApsPageView(generic.TemplateView):
    template_name = 'page/aps.html'

    def get_context_data(self, **kwargs):
        context = super(ApsPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'aps')
        return context


class CommunitiesPageView(generic.TemplateView):
    template_name = 'page/communities.html'

    def get_context_data(self, **kwargs):
        context = super(CommunitiesPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'communities')
        return context


def form_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            email = form.cleaned_data['email']
            org = form.cleaned_data['org']
            title = form.cleaned_data['title']
            # checkbox1 = []
            # for i in range(9):
            #     checkbox1[i] = form.cleaned_data.getlist['checkbox[i]']
            message = form.cleaned_data['message']
            template = get_template('contact_template.txt')
            context = Context({
                'fname': fname,
                'lname': lname,
                'email': email,
                'org': org,
                'title': title,
                # 'checkbox': checkbox1,
                'message': message,
            })
            content = template.render(context)
            print content

            # email = EmailMessage(
            #     "New contact form submission",
            #     content,
            #     "Your website" +'',
            #     ['youremail@gmail.com'],
            #     headers = {'Reply-To': contact_email }
            # )

            return HttpResponseRedirect('page/contact')

        else:
            print("Form not valid")
            print(form.errors)
    else:
            form = ContactForm()
    return render(request, 'page/contact.html', {'form': form})


class GetInvolvedPageView(generic.TemplateView):
    template_name = 'page/get_involved.html'

    def get_context_data(self, **kwargs):
        context = super(GetInvolvedPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'get-involved')
        return context


class HomepageView(generic.TemplateView):
    template_name = 'page/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context['images'] = Team.objects.all()
        context['page'] = Pages.objects.filter(slug=u'homepage')
        return context


class InvolvedParticipatesPageView(generic.TemplateView):
    template_name = 'page/involved_participate.html'

    def get_context_data(self, **kwargs):
        context = super(InvolvedParticipatesPageView, self).get_context_data(**kwargs)
        context['ambassadors'] = Ambassadors.objects.filter()
        return context


class JobsPageView(generic.TemplateView):
    template_name = 'page/jobs.html'

    def get_context_data(self, **kwargs):
        context = super(JobsPageView, self).get_context_data(**kwargs)
        current_job = []
        past_job = []
        for jobs in Section.objects.all():
            if jobs.not_active:
                past_job.append(jobs)
            else:
                current_job.append(jobs)
        context['current_job'] = current_job
        context['past_job'] = past_job
        return context

class JournalPageView(generic.TemplateView):
    template_name = 'page/journals.html'

    def get_context_data(self, **kwargs):
        context = super(JournalPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'journals')
        return context

class MissionPageView(generic.TemplateView):
    template_name = 'page/about_mission.html'

    def get_context_data(self, **kwargs):
        context = super(MissionPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'about_mission')
        return context


class NewsPageView(generic.TemplateView):
    template_name = 'page/news.html'

    def get_context_data(self, **kwargs):
        context = super(NewsPageView, self).get_context_data(**kwargs)
        context['news'] = News.objects.all()
        return context


class OsfPageView(generic.TemplateView):
    template_name = 'page/osf.html'

    def get_context_data(self, **kwargs):
        context = super(OsfPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.all()
        return context


class TeamPageView(generic.TemplateView):
    template_name = 'page/COS_team.html'

    def get_context_data(self, **kwargs):
        context = super(TeamPageView, self).get_context_data(**kwargs)
        current_members = []
        alumni_members = []
        for team_member in Team.objects.all():
            if team_member.alumni:
                alumni_members.append(team_member)
            else:
                current_members.append(team_member)
        context['current_members'] = current_members
        context['alumni_members'] = alumni_members
        return context


class PartnersPageView(generic.TemplateView):
    template_name = 'page/about_partners.html'

    def get_context_data(self, **kwargs):
        context = super(PartnersPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'about_partners')
        return context


class PrPageView(generic.TemplateView):

    def get(self, request, item):
        return render_to_response(os.path.join('page', 'pr', item) + '.html')


class PreregPageView(generic.TemplateView):
    template_name = 'page/prereg.html'

    def get_context_data(self, **kwargs):
        context = super(PreregPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.all()
        return context


class PreRegJournalsPageView(generic.TemplateView):
    template_name = 'page/preregjournals.html'

    def get_context_data(self, **kwargs):
        context = super(PreRegJournalsPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'preregjournals')
        return context


class PreRegListedPageView(generic.TemplateView):
    template_name = 'page/getlisted.html'

    def get_context_data(self, **kwargs):
        context = super(PreRegListedPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'getlisted')
        return context


class ServicePageView(generic.TemplateView):
    template_name = 'page/service.html'

    def get_context_data(self, **kwargs):
        context = super(ServicePageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'service')
        return context


class StatsPageView(generic.TemplateView):
    template_name = 'page/stats_consulting.html'

    def get_context_data(self, **kwargs):
        context = super(StatsPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'stats_consulting')
        return context


class SponsorsPageView(generic.TemplateView):
    template_name = 'page/about_sponsors.html'

    def get_context_data(self, **kwargs):
        context = super(SponsorsPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'about_sponsors')
        return context


class TopPageView(generic.TemplateView):
    template_name = 'page/top.html'

    def get_context_data(self, **kwargs):
        context = super(TopPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'top')
        return context


def google_login(request):

    # Fetch the auth_token that we set in our base view
    auth_token = request.session.get('google_auth_token')

    # The code that google sends in case of a successful authentication
    code = request.GET.get('code')

    if code and auth_token:
        # Set the redirect url on the token
        auth_token.redirect_uri = GOOGLE_APPLICATION_REDIRECT_URI

        # Generate the access token
        auth_token.get_access_token(code)

        request.session['google_auth_token'] = auth_token

        # Populate a session variable indicating successful authentication
        request.session[GOOGLE_COOKIE_CONSENT] = code

        # Redirect to your base page
        return redirect(request.session.get(GOOGLE_REDIRECT_SESSION_VAR))

    # If user has not authenticated the app
    return redirect('/')
