---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["17 semt.001.001.03 SecuritiesMessageRejectionV03", "17.4 Message Building Blocks", "17.4.3 Reason <Rsn>"]
file_pages: [373, 374]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.001.001.03"]
---

# 17.4.3 Reason <Rsn>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 373 to 374.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 373

```text
RelatedReference <RltdRef> contains the following elements (see "AdditionalReference3" on
page 4537 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4537
   ReferenceIssuer <RefIssr> [0..1] ± 4537
   MessageName <MsgNm> [0..1] Text 4537
17.4.3 Reason <Rsn>
Presence: [1..1]
Definition: Reason to reject the message.
Reason <Rsn> contains the following RejectionReason23 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [1..1] CodeSet 373
   AdditionalInformation <AddtlInf> [0..1] Text 373
   LinkedMessage <LkdMsg> [0..1] ± 373
17.4.3.1  Reason <Rsn>
Presence: [1..1]
Definition: Reason to reject the message.
Datatype: "MessageRejectedReason1Code" on page 5329
CodeName Name Definition
REFE InvalidOrUnrecognisedReference Request contains an invalid or
unrecognised business reference.
NALO NotAllowedRequest Instructing party is not allowed to ask for
a status for that specific order.
17.4.3.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about the rejection reason.
Datatype: "Max140Text" on page 5402
17.4.3.3  LinkedMessage <LkdMsg>
Presence: [0..1]
Definition: Identification of the invalid or unrecognised reference.
Approved by the Securities SEG on 27 January 2026 semt.001.001.03 SecuritiesMessageRejectionV03
Investment Funds - Maintenance 2025 - 2026 373 May 2026
```

## File page 374

```text
LinkedMessage <LkdMsg> contains one of the following elements (see "LinkedMessage1Choice" on
page 4865 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PreviousReference <PrvsRef> [1..1] ± 4865
Or   OtherReference <OthrRef> [1..1] ± 4866
Or}   RelatedReference <RltdRef> [1..1] ± 4866
Approved by the Securities SEG on 27 January 2026 semt.001.001.03 SecuritiesMessageRejectionV03
Investment Funds - Maintenance 2025 - 2026 374 May 2026
```

