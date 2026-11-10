---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.11 StandingSettlementInstruction <StgSttlmInstr>"]
file_pages: [115, 116]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.11 StandingSettlementInstruction <StgSttlmInstr>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 115 to 116.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 115

```text
related fields is governed by a market practice document.
• Block Trades:
The parent transaction must be identified using the BloclTrade field with code BLPA. The children
transactions must be identified using the code BLCH.
For more details, see the relevant market practice document on www.smpg.info.
3.4.11 StandingSettlementInstruction <StgSttlmInstr>
Presence: [0..1]
Definition: Specifies what settlement standing instruction database is to be used to derive the
settlement parties involved in the transaction.
Impacted by: C51 "VendorPresenceRule"
StandingSettlementInstruction <StgSttlmInstr> contains the following elements (see
"StandingSettlementInstruction13" on page 295 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementStandingInstructionDatabase
<SttlmStgInstrDB>
[1..1] ± 296
   Vendor <Vndr> [0..1] ± 296
   OtherDeliveringSettlementParties <OthrDlvrgSttlmPties> [0..1] ± C36,
C37,
C38,
C39,
C18
297
   OtherReceivingSettlementParties <OthrRcvgSttlmPties> [0..1] ± C36,
C37,
C38,
C39,
C18
299
Constraints
• VendorPresenceRule
If the settlement standing instruction database is a vendor database, then the vendor must be
identified.
On Condition
    /SettlementStandingInstructionDatabase/Code is equal to value 'VendorDatabase'
Following Must be True
    /Vendor Must be present
3.4.12 DeliveringSettlementParties <DlvrgSttlmPties>
Presence: [0..1]
Definition: Specifies the chain of delivering settlement parties.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 115 February 2025
```

## File page 116

```text
Impacted by: C36 "Party2PresenceRule", C37 "Party3PresenceRule", C38 "Party4PresenceRule", C39
"Party5PresenceRule", C18 "DepositoryGuideline"
DeliveringSettlementParties <DlvrgSttlmPties> contains the following elements (see
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
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 116 February 2025
```

