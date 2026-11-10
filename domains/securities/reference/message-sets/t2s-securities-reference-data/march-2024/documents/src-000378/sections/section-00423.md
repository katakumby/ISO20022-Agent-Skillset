---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.2 Message Datatypes", "13.2.2 CodeSet", "13.2.2.24 InvestorType1Code"]
file_pages: [518]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.2.2.24 InvestorType1Code

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 518 to 518.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 518

```text
13.2.2.24  InvestorType1Code
Definition: Specifies the type of investor.
Type: CodeSet
CodeName Name Definition
RETL Retail Investor is a retail investor.
PROF Professional Investor is a professional or institutional
investor.
STAF Staff Investor is an employee.
PPER PhysicalPerson Investor is a physical person.
13.2.2.25  LegalRestrictions1Code
Definition: Specifies the regulatory restrictions applicable to a security.
Type: CodeSet
CodeName Name Definition
USLE USLegal144A Ownership or transfer of an unregistered
security issued, pursuant to US legal
restrictions 144A.
NORE NoRestrictions Ownership or transfer of a security that
is not subject to restrictions.
REST Restrictions Ownership or transfer of a security that
is subject to restrictions, and not
pursuant to 144A.
13.2.2.26  LegalRestrictions2Code
Definition: Specifies the regulatory restrictions applicable to a security.
Type: CodeSet
CodeName Name Definition
JURO JurisdictionOwnership Investors outside this jurisdiction can
purchase this security, for example, a
Reg S security can only be held by an
investor outside the US.
PPLA PrivatePlacements Only investors qualified by the issuer in
this jurisdiction may purchase this
security.
ACRI AccreditedInvestor Only investors qualified by the regulator
in this jurisdiction may purchase this
security.
MARG Margin Issuer defines whether the security may
be purchased with borrowed money (US
and Japan).
PRIV Privilege Privileges, for example, voting rights, of
holding the security may be restricted by
the issuer.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 518 March 2024
```

