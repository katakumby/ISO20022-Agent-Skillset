---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: []
file_pages: [507, 508, 509]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.023.001.13"]
---

# Continuation at file page 507

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 507 to 509.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 507

```text
The parent transaction must be identified using the Block Trade field with code BLPA. The
children
transactions must be identified using the code BLCH.
For more details, see the relevant market practice document on www.smpg.info.
C73 ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber
must contain the XML message identifier of the linked message.
C74 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C75 TradeDateGuideline
In addition to the settlement date (ISO 20022 mandatory), trade date is one of the 10 common
elements recommended by SMPG for equities and fixed income settlement instructions.
For more details, see the relevant market practice document on www.smpg.info.
C76 TradeDateTimeUTCRule
If Trade Date/Time is used with a time or a time + UTC indicator, then it must be the local time
of the place of trade, for example, of the stock exchange, or of the selling broker for OTC.
C77 TwoLegTransactionOpeningClosing1Rule
For settlement of two part transactions (Securities Financing), the opening/initiation and closing/
return of the transaction is confirmed by sending the following combination of
TransactionIdentificationDetails/SecuritiesMovementType codes and SettlementParameters/
SecuritiesTransactionType codes:
Repo Opening
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: Repo (REPU)
Repo Closing
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: Repo (REPU)
Reverse Repo Opening
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: ReverseRepo (RVPO)
Reverse Repo Closing
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 507 March 2026
```

## File page 508

```text
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: ReverseRepo (RVPO)
TriParty Repo Opening
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: TriPartyRepo (TRPO)
TriParty Repo Closing
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: TriPartyRepo (TRPO)
TriParty Reverse Repo Opening
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: TriPartyReverseRepo (TRVO)
TriParty Reverse Repo Closing
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: TriPartyReverseRepo (TRVO)
Securities Lending Initiation
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: SecuritiesLending (SECL)
Securities Lending Return
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: SecuritiesLending (SECL)
Securities Borrowing Initiation
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: SecuritiesBorrowing (SECB)
Securities Borrowing Return
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: SecuritiesBorrowing (SECB).
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 508 March 2026
```

## File page 509

```text
This constraint is defined at the MessageDefinition level.
C78 TwoLegTransactionOpeningClosing2Rule
For settlement of two part transactions (buy-sell back, sell buy-back, collateral in and out), the
opening/initiation and closing/return of the transaction is instructed by sending the following
combination of SettlementTypeAndAdditionalParameters/SecuritiesMovementType codes and
SettlementParameters/SecuritiesTransactionType codes:
Sell-Buy Back: Sell
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: SellBuyBack (SBBK)
Sell-Buy Back: Buy Back
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: SellBuyBack (SBBK)
Buy-Sell Back: Buy
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: BuySellBack (BSBK)
Buy-Sell Back: Sell Back
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: BuySellBack (BSBK)
Collateral (giver) Out Initiation
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: CollateralOut (COLO)
Collateral (giver) Out Return
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: CollateralOut (COLO)
Collateral (taker) In Initiation
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: CollateralIn (COLI)
Collateral (taker) In Return
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 509 March 2026
```

