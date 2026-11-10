---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.1 ModifiedTransactionDetails <ModfdTxDtls>", "32.4.1.9 TransactionDetails <TxDtls>", "32.4.1.9.6 DigitalPaymentSettlement <DgtlPmtSttlm>", "32.4.1.9.6.3 CashSettlementSystemPlace <CshSttlmSysPlc>", "32.4.1.9.6.3.2 AnyBIC <AnyBIC>"]
file_pages: [1165]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.1.9.6.3.2 AnyBIC <AnyBIC>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1165 to 1165.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1165

```text
32.4.1.9.6.3.2  AnyBIC <AnyBIC>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Impacted by: C8 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 2185
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
32.4.1.9.6.3.3  LEI <LEI>
Presence: [1..1]
Definition: Legal entity identification as an alternate identification for a place of safekeeping.
Datatype: "LEIIdentifier" on page 2187
32.4.1.9.7  DeliveringSettlementParties <DlvrgSttlmPties>
Presence: [0..1]
Definition: Identifies the chain of delivering settlement parties.
Impacted by: C41 "Party2PresenceRule", C43 "Party3PresenceRule", C46 "Party4PresenceRule", C49
"Party5PresenceRule"
DeliveringSettlementParties <DlvrgSttlmPties> contains the following elements (see
"SettlementParties125" on page 1751 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [0..1] ± 1752
   Party1 <Pty1> [0..1] ± C18,
C20
1752
   Party2 <Pty2> [0..1] ± C18,
C20
1753
   Party3 <Pty3> [0..1] ± C18,
C20
1753
   Party4 <Pty4> [0..1] ± C18,
C20
1754
   Party5 <Pty5> [0..1] ± C18,
C20
1755
Constraints
• Party2PresenceRule
If Party2 is present, then Party1 must be present.
On Condition
    /Party2 is present
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1165 March 2026
```

