---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.19 ConfirmationRejectedStatus2", "66.1.45.19.1 Reason <Rsn>", "66.1.45.19.1.2 Proprietary <Prtry>"]
file_pages: [5194]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.19.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5194 to 5194.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5194

```text
CodeName Name Definition
IRIN ReceiversIntermediary Receiver's Intermediary is not
recognised or is invalid.
ICAG DeliveringAgent Delivering agent is not recognised or is
invalid.
IDCU DeliverersCustodian Deliverer's Custodian is not recognised
or is invalid.
IDIN DeliverersIntermediary Deliverer's Intermediary is not
recognised or is invalid.
ICTR InvalidCreditTransfer Credit transfer details are incorrect.
DMON SettlementAmount Settlement Amount is invalid.
DDAT SettlementDate Settlement date or transfer date is not
recognised or is invalid.
NSLA NotCompliantWithSLA Confirmation is not compliant with the
service level agreement.
MEUT MissingEUTaxInformation EU tax information is missing.
MCOM MissingCommission Commission information is missing.
MCHA MissingCharge Charge information is missing.
MTAX MissingTaxInformation Tax information is missing.
NATA NotAllowedtoAmend Amendment of order confirmation not
allowed.
ALAT AmendmentTooLate Amendment of order confirmation too
late.
66.1.45.19.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the rejected status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification1" on page 4552 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4552
   Issuer <Issr> [0..1] Text 4552
66.1.45.19.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about the rejected reason.
Datatype: "Max350Text" on page 5403
66.1.45.20  PendingOpeningStatusReason1Choice
Definition: Choice of formats for a pending account opening status reason.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5194 May 2026
```

