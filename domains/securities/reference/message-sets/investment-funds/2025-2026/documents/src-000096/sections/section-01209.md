---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "40.4.15.11.29 SettlementPartiesDetails <SttlmPtiesDtls>", "40.4.15.11.29.5 ReceivingSideDetails <RcvgSdDtls>"]
file_pages: [1674]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.11.29.5 ReceivingSideDetails <RcvgSdDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1674 to 1674.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1674

```text
Datatype: "Max35Text" on page 5403
40.4.15.11.29.5  ReceivingSideDetails <RcvgSdDtls>
Presence: [0..1]
Definition: Chain of receiving settlement parties.
Impacted by: C12 "BookTransferGuideline", C20 "DepositoryGuideline", C38 "Party2PresenceRule",
C39 "Party3PresenceRule", C40 "Party4PresenceRule", C41 "Party5PresenceRule", C47
"SettlementChainGuideline"
ReceivingSideDetails <RcvgSdDtls> contains the following SettlementParties131 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [0..1] ± 1675
   Party1 <Pty1> [0..1] ± 1676
   Party2 <Pty2> [0..1] ± 1676
   Party3 <Pty3> [0..1] ± 1677
   Party4 <Pty4> [0..1] ± 1677
   Party5 <Pty5> [0..1] ± 1678
Constraints
• BookTransferGuideline
In the case of an own account internal transfer, the account of (delivering) Party2 at (delivering)
Party1 must be provided.
For more details, see the relevant market practice document on www.smpg.info.
• DepositoryGuideline
In a delivery, the receiving depository is to be understood as the requested depository of the
receiving counterparty.
In a receive, the delivering depository is to be understood as the requested depository of the
delivering counterparty.
The field must be populated with the BIC of a national or international CSD. When no CSD exists in a
particular market, the stock exchange BIC will be used.
Country code should be used for settlement taking place outside of an institution published in the
PSET's BIC list. This includes physical deliveries and investment funds not settling at a CSD.
The format and content of the settlement party sequences will comply with the market practices
published for the counterparty depository included in the message.
For more details, see the relevant market practice document on www.smpg.info.
• Party2PresenceRule
If Party2 is present, then Party1 must be present.
On Condition
    /Party2 is present
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1674 May 2026
```

