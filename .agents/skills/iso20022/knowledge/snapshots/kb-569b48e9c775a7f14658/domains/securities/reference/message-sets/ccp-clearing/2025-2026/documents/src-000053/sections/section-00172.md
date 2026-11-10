---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["5 MX secl.004.001.04 NetPositionV04", "5.4 Message Building Blocks", "5.4.5 NetPositionReport <NetPosRpt>", "5.4.5.16 TradeLegDetails <TradLegDtls>", "5.4.5.16.19 Broker <Brkr>", "5.4.5.16.19.3 SafekeepingAccount <SfkpgAcct>"]
file_pages: [226]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.004.001.04"]
---

# 5.4.5.16.19.3 SafekeepingAccount <SfkpgAcct>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 226 to 226.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 226

```text
AlternateIdentification <AltrnId> contains the following elements (see AlternatePartyIdentification8 on
page 444 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationType <IdTp> [1..1] ± 444
   Country <Ctry> [1..1] CodeSet   'C5 444
   AlternateIdentification <AltrnId> [1..1] Text 445
5.4.5.16.19.3  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
Datatype: Max35Text on page 493
5.4.5.16.19.4  ProcessingIdentification <PrcgId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction for the party identified.
Datatype: Max35Text on page 493
5.4.5.16.19.5  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides additional information regarding the party.
Impacted by: C2 AdditonalDetailsGuideline
AdditionalInformation <AddtlInf> contains the following elements (see PartyTextInformation1 on
page 449 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeclarationDetails <DclrtnDtls> [0..1] Text 449
   PartyContactDetails <PtyCtctDtls> [0..1] Text 449
   RegistrationDetails <RegnDtls> [0..1] Text 450
Constraints
• AdditonalDetailsGuideline
(Guideline)
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails, RegistrationDetails
and PartyContactDetails must not contain information that can be provided in a structured field.
5.4.5.16.20  TradingParty <TradgPty>
Presence: [1..1]
Definition: Provides the identification of the trading party.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 226
```

