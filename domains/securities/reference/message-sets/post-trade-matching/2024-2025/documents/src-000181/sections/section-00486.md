---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.26 Settlement Chain", "7.1.26.1 SettlementParties121", "7.1.26.1.6 Party5 <Pty5>", "7.1.26.1.6.4 SafekeepingAccount <SfkpgAcct>"]
file_pages: [556, 557]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.26.1.6.4 SafekeepingAccount <SfkpgAcct>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 556 to 557.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 556

```text
AlternateIdentification <AltrnId> contains the following elements (see "AlternatePartyIdentification8"
on page 398 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationType <IdTp> [1..1] ± 398
   Country <Ctry> [1..1] CodeSet C4 398
   AlternateIdentification <AltrnId> [1..1] Text 399
7.1.26.1.6.4  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
Datatype: "Max35Text" on page 669
7.1.26.2  SettlementParties59
Definition: Chain of parties involved in the settlement of a transaction, including receipts and deliveries,
book transfers, treasury deals, or other activities, resulting in the movement of a security or amount of
money from one account to another.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 556 February 2025
```

## File page 557

```text
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
In a receive, the delivering depository is to be understood as the requested depository of the
delivering counterparty.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 557 February 2025
```

