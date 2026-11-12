---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.28 SettlementTypeAndIdentification29", "35.1.14.28.10 CorporateActionEventIdentification <CorpActnEvtId>"]
file_pages: [1519]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.28.10 CorporateActionEventIdentification <CorpActnEvtId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1519 to 1519.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1519

```text
35.1.14.28.10  CorporateActionEventIdentification <CorpActnEvtId>
Presence: [0..1]
Definition: Identification assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 2192
35.1.14.28.11  NonceIdentification <NonceId>
Presence: [0..1]
Definition: Unambiguous identification of a random or semi-random number used once (NONCE)
generated in the frame of a cryptographic communication.
Datatype: "Max35Text" on page 2192
35.1.14.29  TransactionTypeAndAdditionalParameters21
Definition: Securities financing transaction identification information, type (repurchase agreement,
reverse repurchase agreement, securities lending or securities borrowing) and other parameters.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesFinancingTransactionType <SctiesFincgTxTp> [1..1] CodeSet 1519
   Payment <Pmt> [1..1] CodeSet 1519
   CommonIdentification <CmonId> [0..1] Text 1520
   NonceIdentification <NonceId> [0..1] Text 1520
   ReconciliationIndicator <RcncltnInd> [0..1] Indicator 1520
35.1.14.29.1  SecuritiesFinancingTransactionType <SctiesFincgTxTp>
Presence: [1..1]
Definition: Specifies the type of securities financing transaction, that is, repurchase agreement, reverse
repurchase agreement, securities lending or securities borrowing.
Datatype: "SecuritiesFinancingTransactionType2Code" on page 2142
CodeName Name Definition
REPU Repo Relates to a repurchase agreement
transaction.
RVPO ReverseRepo Relates to a reverse repurchase
agreement transaction.
SECB SecuritiesBorrowing Relates to a securities borrowing
operation.
SECL SecuritiesLending Relates to a securities lending operation.
BSBK BuySellBack Relates to a buy sell back transaction.
SBBK SellBuyBack Relates to a sell buy back transaction.
35.1.14.29.2  Payment <Pmt>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1519 March 2026
```

