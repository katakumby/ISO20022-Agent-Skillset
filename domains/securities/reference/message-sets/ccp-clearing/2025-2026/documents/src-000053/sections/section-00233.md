---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["10 MX secl.009.001.03 BuyInConfirmationV03", "10.4 Message Building Blocks", "10.4.4 OriginalSettlementObligation <OrgnlSttlmOblgtn>", "10.4.4.1 CSDTransactionIdentification <CSDTxId>"]
file_pages: [305]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.009.001.03"]
---

# 10.4.4.1 CSDTransactionIdentification <CSDTxId>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 305 to 305.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 305

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementAmount <SttlmAmt> [1..1] ± 313
   RemainingAmountToBeSettled <RmngAmtToBeSttld> [0..1] ± 314
10.4.4.1  CSDTransactionIdentification <CSDTxId>
Presence: [0..1]
Definition: Last reference given by the settlement platform (this is the central securities depository) to
the transaction (non settled instruction).
Datatype: Max35Text on page 493
10.4.4.2  CentralCounterpartyTransactionIdentification <CntrlCtrPtyTxId>
Presence: [0..1]
Definition: Reference of the transaction (non settled instruction) given by the central counterparty.
Datatype: Max35Text on page 493
10.4.4.3  PreviousBuyInIdentification <PrvsBuyInId>
Presence: [0..1]
Definition: Original buy-in identification number in case an event causes a generation of a new buy-in
identification.
Datatype: Max35Text on page 493
10.4.4.4  DeliveryAccount <DlvryAcct>
Presence: [0..1]
Definition: An account opened by the central counterparty in the name of the clearing member within
the account structure, for settlement purposes (gives information about the clearing member account at
central counterparty).
DeliveryAccount <DlvryAcct> contains the following elements (see SecuritiesAccount19 on page 375
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 375
   Type <Tp> [0..1] ± 375
   Name <Nm> [0..1] Text 375
10.4.4.5  SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Definition: Place where the securities are safe-kept, physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository (CSD) or an International Central Securities
Depository (ICSD).
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.009.001.03 BuyInConfirmationV03
March 2026 305
```

