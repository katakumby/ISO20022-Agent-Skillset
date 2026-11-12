---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.9 ConfirmationParties <ConfPties>", "3.4.9.1 Buyer <Buyr>"]
file_pages: [107]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.9.1 Buyer <Buyr>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 107 to 107.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 107

```text
ConfirmationParties <ConfPties> contains the following ConfirmationParties6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Buyer <Buyr> [0..1] ± 107
   Borrower <Brrwr> [0..1] ± 107
   Seller <Sellr> [0..1] ± 108
   Lender <Lndr> [0..1] ± 108
   BrokerOfCredit <BrkrOfCdt> [0..1] ± 109
   IntroducingFirm <IntrdcgFirm> [0..1] ± 109
   StepInFirm <StepInFirm> [0..1] ± 109
   StepOutFirm <StepOutFirm> [0..1] ± 110
   ClearingFirm <ClrFirm> [0..1] ± 110
   ExecutingBroker <ExctgBrkr> [0..1] ± 110
   CMUParty <CMUPty> [0..1] ± 111
   CMUCounterparty <CMUCtrPty> [0..1] ± 111
   AffirmingParty <AffrmgPty> [0..1] ± 112
   TradeBeneficiaryParty <TradBnfcryPty> [0..1] ± 112
3.4.9.1  Buyer <Buyr>
Presence: [0..1]
Definition: Party that buys goods or services, or a financial instrument.
Buyer <Buyr> contains the following elements (see "ConfirmationPartyDetails7" on page 444 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 445
   AlternateIdentification <AltrnId> [0..1] ± 445
   ProcessingIdentification <PrcgId> [0..1] Text 446
   AdditionalInformation <AddtlInf> [0..1] ± C1 446
   InvestorCapacity <InvstrCpcty> [0..1] ± 446
   TradingPartyCapacity <TradgPtyCpcty> [0..1] ± 447
3.4.9.2  Borrower <Brrwr>
Presence: [0..1]
Definition: Party that has applied, met specific requirements, and received a monetary or securities loan
from a lender. The party initiating the request signs a promissory note agreeing to pay the lien holder
back during a specified timeframe for the entire loan amount plus any additional fees. The borrower is
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 107 February 2025
```

