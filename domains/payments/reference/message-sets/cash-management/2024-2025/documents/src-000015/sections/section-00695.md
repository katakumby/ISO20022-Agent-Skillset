---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.2 Message Datatypes", "37.2.2 CodeSet", "37.2.2.58 SystemEventType2Code"]
file_pages: [880]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.2.2.58 SystemEventType2Code

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 880 to 880.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 880

```text
CodeName Name Definition
RCVR Recovery System is not operational during
recovery operations.
ADTW AllowedDowntimeWindow System is not operational during allowed
downtime windows.
37.2.2.58  SystemEventType2Code
Definition: Specifies a type of event related to a system's operation.
Type: CodeSet
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
CRCO CashReservationCutOff Event is the cutoff for the cash
reservation window.
RECC RecCutOff Event is the cutoff for the settlement of
the multilateral balances stemming from
the retail clearing system.
LTGC LTGCutOff Event is the cutoff for the daytime cycle
of the securities settlement system.
LTDC LTDCutOff Event is the cutoff for the settlement of
the cash multilateral balances resulting
from the daylight cycle of the securities
settlement system.
CUSC CustomerCutOff Event is the cutoff for customer
payments.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 880 February 2025
```

