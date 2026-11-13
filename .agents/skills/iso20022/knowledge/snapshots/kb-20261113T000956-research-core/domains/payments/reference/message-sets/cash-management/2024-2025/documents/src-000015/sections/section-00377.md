---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["17 camt.018.001.05 GetBusinessDayInformationV05", "17.3 Constraints"]
file_pages: [524]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.018.001.05"]
---

# 17.3 Constraints

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 524 to 524.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 524

```text
17.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 ReturnCriteriaAndOrSearchCriteriaRule
If ReturnCriteria is not present, then at least one occurrence of SearchCriteria must be present.
If ReturnCriteria is present, then any occurrence of SearchCriteria is optional.
C4 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
17.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
17.4.1 MessageHeader <MsgHdr>
Presence: [1..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader9" on page 810 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 810
   CreationDateTime <CreDtTm> [0..1] DateTime 810
   RequestType <ReqTp> [0..1]  810
{Or     PaymentControl <PmtCtrl> [1..1] CodeSet 810
Or     Enquiry <Enqry> [1..1] CodeSet 811
Or}     Proprietary <Prtry> [1..1] ± 811
17.4.2 BusinessDayInformationQueryDefinition
<BizDayInfQryDef>
Presence: [0..1]
Definition: Defines the business day information query criteria.
Approved by the Payments SEG on 04 February 2025 camt.018.001.05 GetBusinessDayInformationV05
Cash Management - Maintenance 2024 - 2025 524 February 2025
```

