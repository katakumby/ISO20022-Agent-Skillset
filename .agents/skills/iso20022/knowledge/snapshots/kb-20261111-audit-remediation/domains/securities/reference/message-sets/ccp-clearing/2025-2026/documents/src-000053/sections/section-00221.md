---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["9 MX secl.008.001.03 BuyInResponseV03", "9.4 Message Building Blocks", "9.4.3 OriginalSettlementObligationDetails <OrgnlSttlmOblgtnDtls>", "9.4.3.8 NonClearingMember <NonClrMmb>"]
file_pages: [288, 289]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.008.001.03"]
---

# 9.4.3.8 NonClearingMember <NonClrMmb>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 288 to 289.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 288

```text
Note: This field allows clearing member firm to segregate flows coming from clearing counterparty's
clearing system. Indeed, clearing member firms receive messages from the same system (same
sender) and this field allows them to know if the message is related to equities or derivatives.
ClearingSegment <ClrSgmt> contains one of the following elements (see PartyIdentification35Choice
on page 452 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BIC <BIC> [1..1] IdentifierSet   'C4 452
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 452
9.4.3.8  NonClearingMember <NonClrMmb>
Presence: [0..1]
Definition: Provides the identification for the non-clearing member and account.
NonClearingMember <NonClrMmb> contains the following elements (see
PartyIdentificationAndAccount31 on page 450 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 450
   AlternateIdentification <AltrnId> [0..1] ± 450
   AdditionalInformation <AddtlInf> [0..1] ± C3 451
   ClearingAccount <ClrAcct> [0..1] ± 451
9.4.3.9  IntendedSettlementDate <IntnddSttlmDt>
Presence: [0..1]
Definition: Provides the intended settlement date of the position.
Datatype: ISODate on page 487
9.4.3.10  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Provides details about the security identification.
Impacted by:   'C8 DescriptionPresenceRule  ', C9 DescriptionUsageRule, C10 ISINGuideline,
  'C11 ISINPresenceRule  ',   'C12 OtherIdentificationPresenceRule  '
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.008.001.03 BuyInResponseV03
March 2026 288
```

## File page 289

```text
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
SecurityIdentification14 on page 393 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 394
   OtherIdentification <OthrId> [0..*]  395
     Identification <Id> [1..1] Text 395
     Suffix <Sfx> [0..1] Text 395
     Type <Tp> [1..1] ± 395
   Description <Desc> [0..1] Text 395
Constraints
• DescriptionPresenceRule
(Rule)
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
Error handling:
– Error severity: Fatal
– Error Code: X00192
– Error Text: At least one identification must be present.
• DescriptionUsageRule
(Rule)
Description must be used alone as the last resort.
• ISINGuideline
(Rule)
When a ISIN code exist. It is strongly recommended that the ISIN be used.
• ISINPresenceRule
(Rule)
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.008.001.03 BuyInResponseV03
March 2026 289
```

