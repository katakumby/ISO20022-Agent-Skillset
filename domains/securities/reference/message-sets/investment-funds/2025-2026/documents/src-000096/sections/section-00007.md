---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["2 acmt.001.001.08 AccountOpeningInstructionV08", "2.4 Message Building Blocks", "2.4.4 InstructionDetails <InstrDtls>", "2.4.4.1 OpeningType <OpngTp>"]
file_pages: [26]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.001.001.08"]
---

# 2.4.4.1 OpeningType <OpngTp>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 26 to 26.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 26

```text
InstructionDetails <InstrDtls> contains the following InvestmentAccountOpening4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OpeningType <OpngTp> [1..1] ± 26
   AccountApplicationIdentification <AcctApplId> [0..1] Text 26
   ClientReference <ClntRef> [0..1] Text 26
   CounterpartyReference <CtrPtyRef> [0..1] ± 26
   ExistingAccountIdentification <ExstgAcctId> [0..*] ± 27
2.4.4.1  OpeningType <OpngTp>
Presence: [1..1]
Definition: Specifies if the account opening instruction is about a newly created account or a
supplementary account.
OpeningType <OpngTp> contains one of the following elements (see "AccountOpeningType1Choice"
on page 4324 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4324
Or}   Proprietary <Prtry> [1..1] ± 4325
2.4.4.2  AccountApplicationIdentification <AcctApplId>
Presence: [0..1]
Definition: Unique and unambiguous identifier of the account opening request at application level.
Datatype: "Max35Text" on page 5403
2.4.4.3  ClientReference <ClntRef>
Presence: [0..1]
Definition: Unique and unambiguous identification of a transaction, for example, a transfer, as assigned
by the investor or account owner.
Datatype: "Max35Text" on page 5403
2.4.4.4  CounterpartyReference <CtrPtyRef>
Presence: [0..1]
Definition: Unambiguous identification of the transaction, for example, a transfer, as allocated by the
counterparty.
Approved by the Securities SEG on 27 January 2026 acmt.001.001.08 AccountOpeningInstructionV08
Investment Funds - Maintenance 2025 - 2026 26 May 2026
```

