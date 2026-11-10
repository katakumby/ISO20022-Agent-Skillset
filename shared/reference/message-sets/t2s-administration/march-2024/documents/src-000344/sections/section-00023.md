---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["3 admi.006.001.01 ResendRequestV01", "3.3 Constraints"]
file_pages: [28]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.006.001.01"]
---

# 3.3 Constraints

Source: [src-000344](../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 28 to 28.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 28

```text
3.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
3.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
3.4.1 MessageHeader <MsgHdr>
Presence: [1..1]
Definition: Set of elements to identify the resend message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader7" on page 49 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 49
   CreationDateTime <CreDtTm> [0..1] DateTime 50
   RequestType <ReqTp> [0..1]  50
{Or     PaymentControl <PmtCtrl> [1..1] CodeSet 50
Or     Enquiry <Enqry> [1..1] CodeSet 50
Or}     Proprietary <Prtry> [1..1] ± 50
   OriginalBusinessQuery <OrgnlBizQry> [0..1] ± 51
   QueryName <QryNm> [0..1] Text 51
3.4.2 ResendSearchCriteria <RsndSchCrit>
Presence: [1..*]
Definition: Defines the criteria to unambiguously identify the information to be resent.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
admi.006.001.01 ResendRequestV01
Target2-Securities - Administration - Maintenance 2023 -
2024
28 March 2024
```

