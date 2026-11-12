---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.80 AdditionalParameters24"]
file_pages: [1627]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.80 AdditionalParameters24

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1627 to 1627.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1627

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.80  AdditionalParameters24
Definition: Specifies additional parameters to the message or transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PreConfirmation <PreConf> [0..1] CodeSet 1627
   PartialSettlement <PrtlSttlm> [0..1] CodeSet 1627
   PreviousPartialConfirmationIdentification
<PrvsPrtlConfId>
[0..1] Text 1628
Constraints
• PartialSettlementGuideline
Partial settlement information only applies to markets where partial settlement is allowed.
The PartialSettlement field should be used as follows:
- with code PAIN in the first message(s) (there may be more than one) confirming the partial
settlement of an instruction.
- with code PARC in the very last message sent to confirm the settlement of the remaining part.
For more details, see the relevant market practice document on www.smpg.info.
35.1.16.80.1  PreConfirmation <PreConf>
Presence: [0..1]
Definition: Specifies whether there exists a pre-confirmation.
Datatype: "PreConfirmation1Code" on page 2111
CodeName Name Definition
PRCA PreConfirmCash Pre-confirmation of the movement of the
cash, pending the movement of
securities.
PRSE PreConfirmSecurities Pre-confirmation of the movement of the
securities, pending the movement of
cash.
35.1.16.80.2  PartialSettlement <PrtlSttlm>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1627 March 2026
```

