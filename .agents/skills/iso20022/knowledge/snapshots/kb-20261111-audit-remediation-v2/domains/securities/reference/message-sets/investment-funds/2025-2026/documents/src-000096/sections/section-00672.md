---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.19 PaymentDetails <PmtDtls>", "34.4.4.19.4 CashSettlementDetails <CshSttlmDtls>", "34.4.4.19.4.1 CreditTransferDetails <CdtTrfDtls>", "34.4.4.19.4.1.7 IntermediaryAgent2 <IntrmyAgt2>", "34.4.4.19.4.1.7.1 BICFI <BICFI>"]
file_pages: [913]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.19.4.1.7.1 BICFI <BICFI>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 913 to 913.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 913

```text
IntermediaryAgent2 <IntrmyAgt2> contains the following FinancialInstitutionIdentification16
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BICFI <BICFI> [0..1] IdentifierSet C6 913
   ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 913
   NameAndAddress <NmAndAdr> [0..1] ± 914
   LEI <LEI> [0..1] IdentifierSet 914
   ProprietaryIdentification <PrtryId> [0..1] Text 915
   BranchIdentification <BrnchId> [0..1] ± 915
34.4.4.19.4.1.7.1  BICFI <BICFI>
Presence: [0..1]
Definition: Identification of the financial institution expressed as a BIC.
Impacted by: C6 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 5390
Constraints
• BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
34.4.4.19.4.1.7.2  ClearingSystemMemberIdentification <ClrSysMmbId>
Presence: [0..1]
Definition: Information used to identify a member within a clearing system.
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 913 May 2026
```

