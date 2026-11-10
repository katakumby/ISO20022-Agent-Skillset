---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["4 acmt.003.001.08 AccountModificationInstructionV08", "4.4 Message Building Blocks", "4.4.3 InstructionDetails <InstrDtls>", "4.4.3.1 ModificationReason <ModRsn>"]
file_pages: [64]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.003.001.08"]
---

# 4.4.3.1 ModificationReason <ModRsn>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 64 to 64.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 64

```text
Definition: Information about the modification instruction.
Impacted by: C18 "InstructionDetailsElementRule"
InstructionDetails <InstrDtls> contains the following InvestmentAccountModification4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ModificationReason <ModRsn> [0..1] Text 64
   AccountApplicationIdentification <AcctApplId> [0..1] Text 64
   ClientReference <ClntRef> [0..1] Text 64
   CounterpartyReference <CtrPtyRef> [0..1] ± 64
   ExistingAccountIdentification <ExstgAcctId> [0..*] ± 65
Constraints
• InstructionDetailsElementRule
One of the elements (ModificationReason, AccountApplicationIdentification, ClientReference,
CounterpartyReference, ExistingAccountIdentification) must be present.
4.4.3.1  ModificationReason <ModRsn>
Presence: [0..1]
Definition: Reason for the modification to the investment account information.
Datatype: "Max350Text" on page 5403
4.4.3.2  AccountApplicationIdentification <AcctApplId>
Presence: [0..1]
Definition: Unique and unambiguous identifier of the account modification request.
Datatype: "Max35Text" on page 5403
4.4.3.3  ClientReference <ClntRef>
Presence: [0..1]
Definition: Unique and unambiguous investor's identification of a transfer.
Datatype: "Max35Text" on page 5403
4.4.3.4  CounterpartyReference <CtrPtyRef>
Presence: [0..1]
Definition: Unambiguous identification of the transaction, for example, a transfer, as allocated by the
counterparty.
Approved by the Securities SEG on 27 January 2026 acmt.003.001.08 AccountModificationInstructionV08
Investment Funds - Maintenance 2025 - 2026 64 May 2026
```

