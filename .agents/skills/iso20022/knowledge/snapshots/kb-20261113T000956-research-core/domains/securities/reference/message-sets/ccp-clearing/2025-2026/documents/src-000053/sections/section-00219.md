---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["9 MX secl.008.001.03 BuyInResponseV03", "9.4 Message Building Blocks", "9.4.3 OriginalSettlementObligationDetails <OrgnlSttlmOblgtnDtls>", "9.4.3.5 SafekeepingPlace <SfkpgPlc>", "9.4.3.5.3 TypeAndIdentification <TpAndId>", "9.4.3.5.3.2 Identification <Id>"]
file_pages: [286]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.008.001.03"]
---

# 9.4.3.5.3.2 Identification <Id>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 286 to 286.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 286

```text
CodeName Name Definition
SHHE SharesHeldElsewhere Used for certain financial instruments, for
example, US mutual funds, where
settlement is internal only, that is, there
is no external movement of securities.
9.4.3.5.3.2  Identification <Id>
Presence: [1..1]
Definition: Place of safekeeping.
Impacted by:   'C4 AnyBIC  '
Datatype: AnyBICIdentifier on page 488
Constraints
• AnyBIC
(Rule)
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered by the ISO 9362 Registration Authority in the BIC directory, and
consists of eight (8) or eleven (11) contiguous characters.
Error handling:
– Error severity: Fatal
– Error Code: D00008
– Error Text: Invalid BIC.
9.4.3.5.4  Proprietary <Prtry>
Presence: [1..1]
Definition: Place of safekeeping expressed with a propriety identification scheme.
Proprietary <Prtry> contains the following GenericIdentification58 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 286
   Type <Tp> [1..1]  287
     Identification <Id> [1..1] Text 287
     Issuer <Issr> [1..1] Text 287
     SchemeName <SchmeNm> [0..1] Text 287
9.4.3.5.4.1  Identification <Id>
Presence: [0..1]
Definition: Name or number assigned by an entity to enable recognition of that entity.
Datatype: Max35Text on page 493
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.008.001.03 BuyInResponseV03
March 2026 286
```

