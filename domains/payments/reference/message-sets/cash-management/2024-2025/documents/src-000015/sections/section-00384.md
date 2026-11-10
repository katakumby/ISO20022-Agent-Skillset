---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["17 camt.018.001.05 GetBusinessDayInformationV05", "17.4 Message Building Blocks", "17.4.2 BusinessDayInformationQueryDefinition <BizDayInfQryDef>", "17.4.2.2 Criteria <Crit>", "17.4.2.2.2 NewCriteria <NewCrit>", "17.4.2.2.2.2 SearchCriteria <SchCrit>", "17.4.2.2.2.2.4 EventType <EvtTp>", "17.4.2.2.2.2.4.2 Proprietary <Prtry>"]
file_pages: [531]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.018.001.05"]
---

# 17.4.2.2.2.2.4.2 Proprietary <Prtry>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 531 to 531.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 531

```text
CodeName Name Definition
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
IBKC InterbankCutOff Event is the cutoff for interbank
payments.
SYSC SystemCutOff Event is the cutoff for the system.
SSSC NetSSSReservationCutOff Event is the cutoff for the securities
settlement system cash reservation
window.
REOP ResumeOperation Event is the expected resume time for a
TARGET component.
PCOT ProcessingCutOffTime Event is the cutoff time for the
processing of payments.
NPCT NewPaymentCutOffTime Event is the cutoff time for the receipt of
new commercial payments.
ESTF EndOfStandingFacilities Event is the cut off for the standing
facilities.
17.4.2.2.2.2.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of system event that has occurred, expressed as free text or a bilaterally agreed code.
.
Proprietary <Prtry> contains the following elements (see "GenericIdentification1" on page 809 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 809
   SchemeName <SchmeNm> [0..1] Text 809
   Issuer <Issr> [0..1] Text 809
17.4.2.2.2.2.5  ClosurePeriod <ClsrPrd>
Presence: [0..1]
Definition: Period of time when the system is closed/not operating.
Approved by the Payments SEG on 04 February 2025 camt.018.001.05 GetBusinessDayInformationV05
Cash Management - Maintenance 2024 - 2025 531 February 2025
```

