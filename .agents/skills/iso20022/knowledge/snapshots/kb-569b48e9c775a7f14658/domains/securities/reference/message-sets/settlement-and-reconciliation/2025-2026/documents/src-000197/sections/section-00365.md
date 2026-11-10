---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "17.4 Message Building Blocks", "17.4.15 OtherAmounts <OthrAmts>", "17.4.16.3 CashSettlementSystemPlace <CshSttlmSysPlc>", "17.4.16.3.1 DigitalLedgerIdentification <DgtlLdgrId>"]
file_pages: [548]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.023.001.13"]
---

# 17.4.16.3.1 DigitalLedgerIdentification <DgtlLdgrId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 548 to 548.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 548

```text
Definition: Location where the payment is/will be taking place.
CashSettlementSystemPlace <CshSttlmSysPlc> contains one of the following
CashSettlementSystemPlace1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 548
Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C8 548
Or}   LEI <LEI> [1..1] IdentifierSet 548
17.4.16.3.1  DigitalLedgerIdentification <DgtlLdgrId>
Presence: [1..1]
Definition: Place of safekeeping expressed with a Digital Ledger Identifier. It identifies a digital ledger or
distributed ledger system (for example, blockchain or similar platforms).
Datatype: "DTI2024Identifier" on page 2186
17.4.16.3.2  AnyBIC <AnyBIC>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Impacted by: C8 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 2185
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
17.4.16.3.3  LEI <LEI>
Presence: [1..1]
Definition: Legal entity identification as an alternate identification for a place of safekeeping.
Datatype: "LEIIdentifier" on page 2187
17.4.17 OtherBusinessParties <OthrBizPties>
Presence: [0..1]
Definition: Other business parties relevant to the transaction.
Impacted by: C33 "InvestorCountryCodeRule", C51 "QualifiedForeignIntermediaryRule"
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 548 March 2026
```

