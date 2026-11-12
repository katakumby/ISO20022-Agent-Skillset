---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.11 CommissionWaiverIndicator <ComssnWvrInd>"]
file_pages: [73]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.11 CommissionWaiverIndicator <ComssnWvrInd>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 73 to 73.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 73

```text
2.4.2.15.11  CommissionWaiverIndicator <ComssnWvrInd>
Presence: [0..1]
Definition: Indicates whether the transaction is exempt from commission.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 911):
• Meaning When True: Yes
• Meaning When False: No
2.4.2.15.12  AdditionalInformationIndicator <AddtlInfInd>
Presence: [0..1]
Definition: Indicates whether the underlying transaction details are provided through a separate
message, as in the case of aggregate bookings.
AdditionalInformationIndicator <AddtlInfInd> contains the following MessageIdentification2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageNameIdentification <MsgNmId> [0..1] Text 73
   MessageIdentification <MsgId> [0..1] Text 73
2.4.2.15.12.1  MessageNameIdentification <MsgNmId>
Presence: [0..1]
Definition: Specifies the message name identifier of the message that will be used to provide additional
details.
Datatype: "Max35Text" on page 916
2.4.2.15.12.2  MessageIdentification <MsgId>
Presence: [0..1]
Definition: Specifies the identification of the message that will be used to provide additional details.
Datatype: "Max35Text" on page 916
2.4.2.15.13  AmountDetails <AmtDtls>
Presence: [0..1]
Definition: Provides information on the original amount.
Usage: This component (on entry level) should be used when a total original batch or aggregate
amount has to be provided. If required, the individual original amounts can be included in the same
component on transaction details level.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
73 March 2026
```

