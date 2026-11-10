---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.13 ReceivingSettlementParties <RcvgSttlmPties>"]
file_pages: [117, 118]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.13 ReceivingSettlementParties <RcvgSttlmPties>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 117 to 118.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 117

```text
Constraints
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
Following Must be True
    /Party1 Must be present
• Party3PresenceRule
If Party3 is present, then Party2 must be present.
On Condition
    /Party3 is present
Following Must be True
    /Party2 Must be present
• Party4PresenceRule
If Party4 is present, then Party3 must be present.
On Condition
    /Party4 is present
Following Must be True
    /Party3 Must be present
• Party5PresenceRule
If Party5 is present, then Party4 must be present.
On Condition
    /Party5 is present
Following Must be True
    /Party4 Must be present
3.4.13 ReceivingSettlementParties <RcvgSttlmPties>
Presence: [0..1]
Definition: Specifies the chain of receiving settlement parties.
Impacted by: C36 "Party2PresenceRule", C37 "Party3PresenceRule", C38 "Party4PresenceRule", C39
"Party5PresenceRule", C18 "DepositoryGuideline"
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 117 February 2025
```

## File page 118

```text
ReceivingSettlementParties <RcvgSttlmPties> contains the following elements (see
"SettlementParties59" on page 556 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [0..1] ± 558
   Party1 <Pty1> [0..1]  C5 559
     Identification <Id> [1..1] ± 559
     AdditionalInformation <AddtlInf> [0..1] Text 560
     AlternateIdentification <AltrnId> [0..1] ± 560
     SafekeepingAccount <SfkpgAcct> [0..1] Text 560
   Party2 <Pty2> [0..1]  C5 561
     Identification <Id> [1..1] ± 561
     AdditionalInformation <AddtlInf> [0..1] Text 562
     AlternateIdentification <AltrnId> [0..1] ± 562
     SafekeepingAccount <SfkpgAcct> [0..1] Text 562
   Party3 <Pty3> [0..1]  C5 563
     Identification <Id> [1..1] ± 563
     AdditionalInformation <AddtlInf> [0..1] Text 564
     AlternateIdentification <AltrnId> [0..1] ± 564
     SafekeepingAccount <SfkpgAcct> [0..1] Text 564
   Party4 <Pty4> [0..1]  C5 565
     Identification <Id> [1..1] ± 565
     AdditionalInformation <AddtlInf> [0..1] Text 566
     AlternateIdentification <AltrnId> [0..1] ± 566
     SafekeepingAccount <SfkpgAcct> [0..1] Text 566
   Party5 <Pty5> [0..1]  C5 567
     Identification <Id> [1..1] ± 567
     AdditionalInformation <AddtlInf> [0..1] Text 568
     AlternateIdentification <AltrnId> [0..1] ± 568
     SafekeepingAccount <SfkpgAcct> [0..1] Text 568
Constraints
• DepositoryGuideline
In a delivery, the receiving depository is to be understood as the requested depository of the
receiving counterparty.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 118 February 2025
```

