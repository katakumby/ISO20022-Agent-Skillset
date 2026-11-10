---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["17 semt.001.001.03 SecuritiesMessageRejectionV03", "17.2 Structure"]
file_pages: [372]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.001.001.03"]
---

# 17.2 Structure

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 372 to 372.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 372

```text
17.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesMsgRjctn> [1..1]  
   MessageIdentification <MsgId> [1..1] ± 372
   RelatedReference <RltdRef> [1..1] ± 372
   Reason <Rsn> [1..1]  373
     Reason <Rsn> [1..1] CodeSet 373
     AdditionalInformation <AddtlInf> [0..1] Text 373
     LinkedMessage <LkdMsg> [0..1] ± 373
17.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered by the ISO 9362 Registration Authority in the BIC directory,
and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
17.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
17.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies a message from a business application standpoint.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
17.4.2 RelatedReference <RltdRef>
Presence: [1..1]
Definition: Reference to a linked message that was previously received.
Approved by the Securities SEG on 27 January 2026 semt.001.001.03 SecuritiesMessageRejectionV03
Investment Funds - Maintenance 2025 - 2026 372 May 2026
```

