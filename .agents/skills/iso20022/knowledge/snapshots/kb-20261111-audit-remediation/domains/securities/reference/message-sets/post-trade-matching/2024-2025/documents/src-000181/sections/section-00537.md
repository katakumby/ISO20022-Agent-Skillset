---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.11 BorrowingReason1Code"]
file_pages: [616]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.11 BorrowingReason1Code

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 616 to 616.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 616

```text
CodeName Name Definition
BLCH Child Transaction is a block trade child.
7.2.2.11  BorrowingReason1Code
Definition: Identifies the underlying reason for the borrowing.
Type: CodeSet
CodeName Name Definition
SFCT SelfConsumption The borrowing reason is for Self
consumption.
TTTP TransferToThirdParty The borrowing reason is for Transfer to
thrid party.
MMPP MarketMakingPurpose The borrowing reason is for Market
making purpose.
7.2.2.12  BusinessProcessType1Code
Definition: Type of business process model used to carry out the transaction.
Type: CodeSet
CodeName Name Definition
ISUP TripartiteCentralMatching Specifies the processing of a transaction
in a central matching utility model.
NISP NotCoveredByInvestmentInstructions Specifies the processing of a transaction
in a local matching model.
PRAC PreAccepted Transaction notice results from an
agreement made out of a trading
platform between two members (broker
and intermediary) of an authorised entity.
RSAL Reversal Transaction notice reverses a previously
sent and agreed transaction notice. If the
reversal transaction notice is stated to
serve as invoice:
o Fees and taxes contained in the
transaction notice are considered as
being in debit of the broker's account
and in credit of the intermediary's
account: it is a 'credit invoice';
o The broker will have to specify the
original transaction notice reference;
o The reversal transaction notice will
have the same direction (buy, sell) as
the original transaction notice.
PROP OwnAccountTradeType Specifies the processing of a transaction
in a own account trade type model.
THRU ThroughType Specifies the processing of a transaction
in a through type model.
IDEL BillateralCentralMatching Specifies the processing of a transaction
in a billateral central matching model.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 616 February 2025
```

