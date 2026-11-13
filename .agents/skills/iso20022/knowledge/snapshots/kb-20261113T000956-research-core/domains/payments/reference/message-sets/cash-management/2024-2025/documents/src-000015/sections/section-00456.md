---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["23 camt.025.001.09 ReceiptV09", "23.4 Message Building Blocks", "23.4.2 ReceiptDetails <RctDtls>", "23.4.2.2 OriginalPaymentIdentification <OrgnlPmtId>", "23.4.2.2.4 LongBusinessIdentification <LngBizId>", "23.4.2.2.4.7 InstructedAgent <InstdAgt>"]
file_pages: [615]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.025.001.09"]
---

# 23.4.2.2.4.7 InstructedAgent <InstdAgt>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 615 to 615.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 615

```text
InstructingAgent <InstgAgt> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 803 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  804
     BICFI <BICFI> [0..1] IdentifierSet C2 804
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 805
     LEI <LEI> [0..1] IdentifierSet 805
     Name <Nm> [0..1] Text 805
     PostalAddress <PstlAdr> [0..1] ± 805
     Other <Othr> [0..1] ± 806
   BranchIdentification <BrnchId> [0..1]  807
     Identification <Id> [0..1] Text 807
     LEI <LEI> [0..1] IdentifierSet 807
     Name <Nm> [0..1] Text 807
     PostalAddress <PstlAdr> [0..1] ± 807
23.4.2.2.4.7  InstructedAgent <InstdAgt>
Presence: [1..1]
Definition: Agent that is instructed by the previous party in the chain to carry out the (set of)
instruction(s).
Approved by the Payments SEG on 04 February 2025 camt.025.001.09 ReceiptV09
Cash Management - Maintenance 2024 - 2025 615 February 2025
```

