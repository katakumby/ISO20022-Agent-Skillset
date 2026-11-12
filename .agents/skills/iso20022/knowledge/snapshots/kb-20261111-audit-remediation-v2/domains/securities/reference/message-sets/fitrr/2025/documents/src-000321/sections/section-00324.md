---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.2 SecuritiesTransactionReport7", "22.1.13.2.9 FinancialInstrument <FinInstrm>", "22.1.13.2.9.1 Identification <Id>"]
file_pages: [378]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.2.9.1 Identification <Id>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 378 to 378.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 378

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Interest <Intrst> [1..1] ± 388
           ForeignExchange <FX> [1..1] ± 388
22.1.13.2.9.1  Identification <Id>
Presence: [1..1]
Definition: Identification of a financial instrument admitted to trading.
Datatype: "ISINOct2015Identifier" on page 450
22.1.13.2.9.2  AlternateIdentification <AltrnId>
Presence: [1..1]
Definition: Identification of a financial instrument admitted to trading for which an alternate identification
is available, such as a tokenized instrument identified by both an ISIN and a digital token identifier
(DTI).
Impacted by: C5 "DescriptionPresenceRule", C6 "DescriptionUsageRule", C7 "ISINGuideline", C8
"ISINPresenceRule", C11 "OtherIdentificationPresenceRule"
AlternateIdentification <AltrnId> contains the following elements (see "SecurityIdentification19" on
page 329 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 330
   OtherIdentification <OthrId> [0..*]  330
     Identification <Id> [1..1] Text 330
     Suffix <Sfx> [0..1] Text 330
     Type <Tp> [1..1] ± 330
   Description <Desc> [0..1] Text 331
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
• DescriptionUsageRule
Description must be used alone as the last resort.
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
378 July 2025
```

