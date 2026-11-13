---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks", "5.4.9 CorporateActionInstruction <CorpActnInstr>", "5.4.9.10 CurrencyOption <CcyOptn>"]
file_pages: [308]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4.9.10 CurrencyOption <CcyOptn>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 308 to 308.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 308

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
5.4.9.10  CurrencyOption <CcyOptn>
Presence: [0..1]
Definition: Currency in which cash proceeds are to be credited or debited.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 1157
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
5.4.9.11  SecurityIdentification <SctyId>
Presence: [0..1]
Definition: Identifies the financial instrument.
Impacted by: C10 "DescriptionPresenceRule", C11 "DescriptionUsageRule", C17 "ISINGuideline", C18
"ISINPresenceRule", C23 "OtherIdentificationPresenceRule"
SecurityIdentification <SctyId> contains the following elements (see "SecurityIdentification19" on
page 869 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 870
   OtherIdentification <OthrId> [0..*]  870
     Identification <Id> [1..1] Text 870
     Suffix <Sfx> [0..1] Text 870
     Type <Tp> [1..1] ± 871
   Description <Desc> [0..1] Text 871
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 308 February 2026
```

