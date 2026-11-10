---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.80 TradingCapacity6Code"]
file_pages: [656]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.80 TradingCapacity6Code

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 656 to 656.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 656

```text
7.2.2.80  TradingCapacity6Code
Definition: Specifies the role of a trading party in a transaction.
Type: CodeSet
CodeName Name Definition
AGEN Agent Trading as Agent on behalf of a
customer.
BAGN ActingAgent Party acting as an agent for both
customer and another person.
CAGN CrossingAgent Crossing as an agent.
CPRN CrossingPrincipal Crossing as a principal.
OAGN OtherAgent Acting as an agent for a party other than
a customer.
PRAG PrincipalAgent Acting as an agent for some executions
and principal for others in the same
transaction.
PRIN Principal Trading as Principal.
7.2.2.81  TradingDate1Code
Definition: Trading Date Code.
Type: CodeSet
CodeName Name Definition
VARI Various Partial trades have occurred over a
period of two or more days.
7.2.2.82  TypeOfIdentification1Code
Definition: Specifies the type of alternate identification which can be used to give an alternate
identification of the party identified.
Type: CodeSet
CodeName Name Definition
ARNU AlienRegistrationNumber Number assigned by a government
agency to identify foreign nationals.
CCPT PassportNumber Number assigned by a passport
authority.
CHTY TaxExemptIdentificationNumber Number assigned to a tax exempt entity.
CORP CorporateIdentification Number assigned to a corporate entity.
DRLC DriverLicenseNumber Number assigned to a driver's license.
FIIN ForeignInvestmentIdentityNumber Number assigned to a foreign investor
(other than the alien number).
TXID TaxIdentificationNumber Number assigned by a tax authority to
an entity.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 656 February 2025
```

