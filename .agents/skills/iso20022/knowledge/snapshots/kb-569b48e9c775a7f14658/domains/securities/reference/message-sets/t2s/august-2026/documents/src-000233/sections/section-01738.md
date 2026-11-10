---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["67 reda.051.001.01 AccountLinkStatusAdviceV01", "67.4 Message Building Blocks", "67.4.3 AccountLinkIdentification <AcctLkId>", "67.4.3.3 CashAccount <CshAcct>"]
file_pages: [2387, 2388]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.051.001.01"]
---

# 67.4.3.3 CashAccount <CshAcct>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2387 to 2388.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2387

```text
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 3016 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 3016
   Type <Tp> [0..1] ± 3016
   Name <Nm> [0..1] Text 3016
67.4.3.3  CashAccount <CshAcct>
Presence: [1..1]
Definition: Account to or from which a cash entry is made.
CashAccount <CshAcct> contains the following elements (see "CashAccount38" on page 2828 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 2828
   Type <Tp> [0..1] ± 2828
   Currency <Ccy> [0..1] CodeSet C1 2828
   Name <Nm> [0..1] Text 2829
   Proxy <Prxy> [0..1] ± 2829
67.4.3.4  ValidFrom <VldFr>
Presence: [1..1]
Definition: Defines the date since when the securities account is linked to the cash account.
ValidFrom <VldFr> contains one of the following elements (see "DateAndDateTime2Choice" on
page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
67.4.4 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C7 "SupplementaryDataRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.051.001.01 AccountLinkStatusAdviceV01
Target2-Securities 2387 August 2026
```

## File page 2388

```text
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 3011 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 3011
   Envelope <Envlp> [1..1] (External Schema) 3012
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.051.001.01 AccountLinkStatusAdviceV01
Target2-Securities 2388 August 2026
```

