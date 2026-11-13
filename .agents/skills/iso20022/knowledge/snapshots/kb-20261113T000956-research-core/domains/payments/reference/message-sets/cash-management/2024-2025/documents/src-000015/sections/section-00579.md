---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["33 camt.101.001.02 CreateLimitV02", "33.4 Message Building Blocks", "33.4.2 LimitData <LmtData>", "33.4.2.2 StartDateTime <StartDtTm>"]
file_pages: [753, 754]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.101.001.02"]
---

# 33.4.2.2 StartDateTime <StartDtTm>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 753 to 754.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 753

```text
AccountIdentification <AcctId> contains one of the following elements (see
"AccountIdentification4Choice" on page 787 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C5 787
Or}   Other <Othr> [1..1] ± 788
33.4.2.2  StartDateTime <StartDtTm>
Presence: [0..1]
Definition: Date and time at which the limit becomes effective.
StartDateTime <StartDtTm> contains one of the following elements (see "DateAndDateTime2Choice"
on page 801 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 801
Or}   DateTime <DtTm> [1..1] DateTime 801
33.4.2.3  Amount <Amt>
Presence: [1..1]
Definition: Amount of money of the limit, expressed in an eligible currency.
Amount <Amt> contains one of the following elements (see "Amount2Choice" on page 788 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 788
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 788
33.4.2.4  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Specifies if a limit is a debit limit or a credit limit.
Datatype: "CreditDebitCode" on page 851
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
33.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Approved by the Payments SEG on 04 February 2025 camt.101.001.02 CreateLimitV02
Cash Management - Maintenance 2024 - 2025 753 February 2025
```

## File page 754

```text
Impacted by: C8 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 815 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 816
   Envelope <Envlp> [1..1] (External Schema) 816
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Payments SEG on 04 February 2025 camt.101.001.02 CreateLimitV02
Cash Management - Maintenance 2024 - 2025 754 February 2025
```

