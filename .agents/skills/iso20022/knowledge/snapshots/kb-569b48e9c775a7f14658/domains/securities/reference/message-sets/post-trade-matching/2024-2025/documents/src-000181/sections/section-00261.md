---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.29 BusinessProcessType2Choice", "7.1.19.29.1 Code <Cd>"]
file_pages: [319]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.29.1 Code <Cd>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 319 to 319.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 319

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 319
Or}   Proprietary <Prtry> [1..1] ± 319
7.1.19.29.1  Code <Cd>
Presence: [1..1]
Definition: Business process type is identified using a code.
Datatype: "BusinessProcessType1Code" on page 616
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
DPLX DuplexType Specifies the processing of a transaction
in a duplex type model.
7.1.19.29.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of business process expressed as a proprietary code.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 319 February 2025
```

