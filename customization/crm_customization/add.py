import os

def after_install():
    print('This is custom app running')
    current_working_directory = os.getcwd()
    print(current_working_directory)
    f = open("../../../erpnext/erpnext/public/js/templates/crm_activities.html", "w")
    f.write('''
<div class="open-activities">
	<div class="new-btn pb-3">
		<span>
			<button class="btn btn-sm small new-task-btn mr-1">
				<svg class="icon icon-sm">
					<use href="#icon-small-message"></use>
				</svg>
				{{ __("New Task") }}
			</button>
			<button class="btn btn-sm small new-event-btn">
				<svg class="icon icon-sm">
					<use href="#icon-calendar"></use>
				</svg>
				{{ __("New Event") }}
			</button>
		</span>
	</div>
	<div class="section-body">
		<div class="open-tasks pr-1">
			<div class="open-section-head">
				<span class="ml-2">{{ __("Open Tasks") }}</span>
			</div>
			{% var parents = [] %}
			{% for(var i=0, l=tasks.length; i<l; i++) { %}
				{% if(tasks[i].parent_dict && !parents.includes(tasks[i].parent_dict)){parents.push(tasks[i].parent_dict)} %}
			{% } %}
			{% tasks[i] { %}
			<div class="single-activity">
				{% if (tasks.length) { %}
					{% for(var j=0, k=parents.length; j<k; j++) { %}
						<div class="ml-3 bold p-3 notes-section" onclick="toggleTasks(this)">
							{{ parents[j] }}
						</div>
						<div class="task-list" style="display: none;">
							{% for(var i=0, l=tasks.length; i<l; i++) { %}
								{% if (tasks[i].parent_dict == parents[j]) { %}
									<div class="single-activity mx-5">
										<div class="flex justify-between mb-2">
											<div class="row label-area font-md ml-1">
												<span class="mr-2">
													<svg class="icon icon-sm">
														<use href="#icon-small-message"></use>
													</svg>
												</span>
												<a href="/app/todo/{{ tasks[i].name }}" title="{{ __('Open Task') }}">
													{{ tasks[i].description }}
												</a>
											</div>
											<div class="checkbox">
												<input type="checkbox" class="completion-checkbox"
													name="{{ tasks[i].name }}" title="{{ __('Mark As Closed') }}">
											</div>
										</div>
										{% if (tasks[i].date) { %}
											<div class="text-muted ml-1">
												{{ frappe.datetime.global_date_format(tasks[i].date) }}
											</div>
										{% } %}
										{% if (tasks[i].allocated_to) { %}
											<div class="text-muted  ml-1">
												{{ __("Allocated To:") }}
												{{ tasks[i].allocated_to }}
											</div>
										{% } %}
									</div>
								{% } %}
							{% } %}
						</div>
					{% } %}
				{% } else { %}
					<div class="single-activity no-activity text-muted">
						{{ __("No open task") }}
					</div>
				{% } %}
			</div>
		</div>
</div>


<style>
.open-activities {
	min-height: 50px;
	padding-left: 0px;
	padding-bottom: 15px !important;
}

.open-activities .new-btn {
	text-align: right;
}

.single-activity {
	min-height: 90px;
	border: 1px solid var(--border-color);
	padding: 10px;
	border-bottom: 0;
	padding-right: 0;
}

.single-activity:last-child {
	border-bottom: 1px solid var(--border-color);
}

.single-activity:hover .completion-checkbox{
	display: block;
}

.completion-checkbox {
	vertical-align: middle;
	display: none;
}

.checkbox {
	min-width: 22px;
}

.open-tasks {
	width: 50%;
}

.open-tasks:first-child {
	border-right: 0;
}

.open-events {
	width: 50%;
}

.open-section-head {
	background-color: var(--bg-color);
	min-height: 30px;
	border-bottom: 1px solid var(--border-color);
	padding: 10px;
	font-weight: bold;
}

.no-activity {
    text-align: center;
    padding-top: 30px;
}

.form-footer {
	background-color: var(--bg-color);
}

.notes-section {
	padding: 10px;
	border-radius: 5px;
	cursor: pointer;
	transition: background-color 0.3s ease;
}

.notes-section:hover {
	background-color: #f0f0f0;
}
</style>

<script>
    function toggleTasks(element) {
        var taskList = element.nextElementSibling;
        if (taskList.style.display === "none" || taskList.style.display === "") {
            taskList.style.display = "block";
        } else {
            taskList.style.display = "none";
        }
    }
</script>



''')
    f.close()