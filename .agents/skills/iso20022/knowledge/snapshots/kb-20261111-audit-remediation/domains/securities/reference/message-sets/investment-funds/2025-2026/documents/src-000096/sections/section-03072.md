---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03", "64.4 Message Building Blocks", "64.4.3 IndividualOrderConfirmationDetailsReport <IndvOrdrConfDtlsRpt>", "64.4.3.3 Confirmation <Conf>", "64.4.3.3.1 ConfirmationRejected <ConfRjctd>"]
file_pages: [4291]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.057.001.03"]
---

# 64.4.3.3.1 ConfirmationRejected <ConfRjctd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4291 to 4291.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4291

```text
Confirmation <Conf> contains one of the following ConfirmationStatus1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ConfirmationRejected <ConfRjctd> [1..10] ± C8 4291
Or   AmendmentRejected <AmdmntRjctd> [1..10] ± C8 4291
Or}   Status <Sts> [1..1] CodeSet 4292
64.4.3.3.1  ConfirmationRejected <ConfRjctd>
Presence: [1..10]
Definition: Status of the order confirmation is rejected.
Impacted by: C8 "ReasonElementRule"
ConfirmationRejected <ConfRjctd> contains the following elements (see
"ConfirmationRejectedStatus2" on page 5191 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1]  5191
{Or     Code <Cd> [1..1] CodeSet 5192
Or}     Proprietary <Prtry> [1..1] ± 5194
   AdditionalInformation <AddtlInf> [0..1] Text 5194
Constraints
• ReasonElementRule
Either Reason or AdditionalInformation must be present. Both may be present.
64.4.3.3.2  AmendmentRejected <AmdmntRjctd>
Presence: [1..10]
Definition: Status of the order confirmation amendment is rejected.
Impacted by: C8 "ReasonElementRule"
AmendmentRejected <AmdmntRjctd> contains the following elements (see
"ConfirmationRejectedStatus2" on page 5191 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1]  5191
{Or     Code <Cd> [1..1] CodeSet 5192
Or}     Proprietary <Prtry> [1..1] ± 5194
   AdditionalInformation <AddtlInf> [0..1] Text 5194
Approved by the Securities SEG on 27 January 2026 setr.057.001.03 OrderConfirmationStatusReportV03
Investment Funds - Maintenance 2025 - 2026 4291 May 2026
```

