---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["35 camt.103.001.03 CreateReservationV03", "35.2 Structure"]
file_pages: [768]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.103.001.03"]
---

# 35.2 Structure

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 768 to 768.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 768

```text
35.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <CretRsvatn> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 769
   ReservationIdentification <RsvatnId> [1..1]  769
     ReservationIdentification <RsvatnId> [0..1] Text 769
     SystemIdentification <SysId> [0..1] ± 769
     Type <Tp> [1..1]  770
{Or       Code <Cd> [1..1] CodeSet 770
Or}       Proprietary <Prtry> [1..1] Text 770
     AccountOwner <AcctOwnr> [0..1] ± 770
     AccountIdentification <AcctId> [0..1] ± 771
   ValueSet <ValSet> [1..1] ± 771
   SupplementaryData <SplmtryData> [0..*] ± C6 772
35.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C3 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C4 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C5 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
Approved by the Payments SEG on 04 February 2025 camt.103.001.03 CreateReservationV03
Cash Management - Maintenance 2024 - 2025 768 February 2025
```

