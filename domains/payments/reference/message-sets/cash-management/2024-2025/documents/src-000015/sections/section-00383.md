---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["17 camt.018.001.05 GetBusinessDayInformationV05", "17.4 Message Building Blocks", "17.4.2 BusinessDayInformationQueryDefinition <BizDayInfQryDef>", "17.4.2.2 Criteria <Crit>", "17.4.2.2.2 NewCriteria <NewCrit>", "17.4.2.2.2.2 SearchCriteria <SchCrit>", "17.4.2.2.2.2.4 EventType <EvtTp>"]
file_pages: [530]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.018.001.05"]
---

# 17.4.2.2.2.2.4 EventType <EvtTp>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 530 to 530.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 530

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
17.4.2.2.2.2.4  EventType <EvtTp>
Presence: [0..1]
Definition: Nature of the event that has occurred.
EventType <EvtTp> contains one of the following SystemEventType2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 530
Or}   Proprietary <Prtry> [1..1] ± 531
17.4.2.2.2.2.4.1  Code <Cd>
Presence: [1..1]
Definition: Type of system event that has occurred, expressed in a coded form.
Datatype: "SystemEventType2Code" on page 880
CodeName Name Definition
LVCO LVPCutOff Event is the cutoff time for low value
payments processed by the system.
LVCC LVPCancellationCutOff Event is the cutoff time after which low
value payments can no longer be
cancelled.
LVRT LVPCutOffReportTime Event is the time at which the members
will be provided with the report
corresponding to the processing of low
value payments.
EUSU Euro1StartUp Event is the opening of the Euro 1
system operation.
STSU Step1StartUp Event is the start of the Step 1 system
operation.
LWSU LimitWarningStartUp Event is the start of the limit warning
period.
EUCO Euro1CutOff Event is the cutoff time for the Euro1
system, that is, the deadline for
processing Euro1 transactions.
FIRE FinalReporting Event is the report after all operations
have ceased in the system.
STDY StartOfDay Event is the start of the operating day.
LTNC LTNCutOff Event is the cutoff for the settlement of
the cash multilateral balances resulting
from the overnight cycle of the securities
settlement system.
Approved by the Payments SEG on 04 February 2025 camt.018.001.05 GetBusinessDayInformationV05
Cash Management - Maintenance 2024 - 2025 530 February 2025
```

