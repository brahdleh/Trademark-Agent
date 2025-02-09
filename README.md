# IP Agent
For the Oxford Eth 2025 hackathon we have created a Python bot that can help legal firms find infringement in trademark requests.

Given a proposed name and a description of the company's goods and services, the Agent:

1. gathers data on the different trademark classes from the internet.
2. assigns classes based on the company summary provided.
3. Scrapes similarly named trademarks from the EU IP website using Selenium.
4. Filters the results for those with overlapping goods and services.
5. Applies a formula to assess string similarity
6. Writes a report on any potential infringement.

This Github houses the code ready to be deployed to the cloud as an API, but this is not currently running.

Please view the code in this Google Colab notebook, which contains the 3 real demos you see in this ReadMe.

[Google Colab](https://colab.research.google.com/drive/1flKc7FvMSHKr6hqF4MB13d16IHkdw9bo?usp=sharing) 

---

## Demo 1 - Can I create a computer hardware company called Apple?

**Input name:** Apple

**Input summary:** The company manufactures and sells computer hardware, along with offering repairs and maintenance

---

#### Agent Response:

### Trademark Infringement Audit

**Date:** February 9th, 2025

This audit concerns the proposed trademark "APPLE" and its potential for infringement within the following Nice Classes:

**Class 9:** Broadly covers scientific, technological, and computer-related apparatus, instruments, software, and accessories.

**Class 37:** Covers building construction, repair, and installation services, including those related to computer hardware.

**Class 42:** Covers scientific and technological services, research and design, computer programming, consultancy, and website-related services.
Conflict Details:

The following trademarks have been flagged as potential conflicts due to their similarity to the proposed trademark "APPLE":

**Exact Matches:**

APPLE

**Recommended Actions:**

Given the presence of identical trademark registrations, the following actions are recommended to mitigate the risk of infringement:

**Modify Application:** The client should consider modifying the proposed trademark to distinguish it from the existing registrations. This could involve adding a distinctive element (word, logo, or design) to the trademark "APPLE". This should be a discussion with the client.

**Consult Legal Advice:** Engaging with an experienced EU IP lawyer is crucial. A legal professional can conduct a more in-depth analysis of the existing trademark landscape, assess the specific risks of infringement in each relevant class, and advise on the most appropriate course of action.

**Negotiate with Holder:** Depending on the scope of the existing trademark registrations and the client's specific business activities, it may be possible to negotiate a co-existence agreement or other form of arrangement with the trademark holders. This could allow the client to use the "APPLE" trademark in a limited manner or within a specific geographic area. This action may prove fruitless due to the volume of matches but could be attempted once consultation has taken place.

It is important to act quickly to determine the best course of action and minimse potential costs or delays from third-party issues.

---

## Demo 2 - Can I create an arms company called Bradcorp

**Input name:** Bradcorp

**Input summary:** The company manufactures and sells arms to foreign governments.

---

#### Agent Response:

### Trademark Infringement Audit

**Date:** February 9th, 2025

**Company Name:** Bradcorp

**Classification Details:**

The relevant class identified for this audit is:

**Class 13:** Encompasses goods such as firearms, ammunition, projectiles, explosives, and fireworks.
Conflict Details:

Based on our search and analysis of existing registered and pending trademarks within the European Union across the specified Class 13, no trademarks were found that are confusingly similar to the proposed name "Bradcorp" for the goods and services listed. Therefore, there is no currently foreseeable or apparent risk of trademark infringement.

**Actions to Secure Trademark:**

To establish and secure exclusive rights to the "Bradcorp" trademark within the European Union for goods in Class 13, the following actions are recommended:

File a European Union Trademark (EUTM) application: A formal application should be filed with the European Union Intellectual Property Office (EUIPO) seeking registration of the "Bradcorp" mark for the specific goods within Class 13 that the client intends to use the mark in connection with.
Monitor the Trademark Register: Continuously monitor the EUIPO trademark register for any newly filed applications that may be similar to "Bradcorp" to proactively address any potential future conflicts.

---

## Demo 3 - A hardware wallet manufacturer called Ledger

**Input name:** Ledger
**Input summary:** The company manufactures and sells Crypto hardware wallets.

---

#### Agent Response:

### Trademark Infringement Audit

**Date:** February 9th, 2025

**Classification Details:**

The client is seeking trademark protection for the name "Ledger" in Class 9, encompassing a wide range of goods including scientific and technological apparatus, data processing equipment, computer software, telecommunications apparatus, and protective clothing.

**Conflict Details:**

The following potentially conflicting trademarks have been identified:

**Exact Matches:** LEDGER, Ledger, LEDGER

**Similar Names:** xledger, XLEDGER

**Recommended Actions:**

Given the presence of exact matches and highly similar names, the following actions are recommended:

**Modify Application:** Consider modifying the application to include a distinctive logo or design element in conjunction with the name "Ledger" to differentiate it from existing trademarks. Alternatively, consider adding a descriptive term to create a composite mark (e.g., "Ledger Tech").

**Consult Legal Advice:** Seek detailed advice from an experienced EU trademark attorney. A comprehensive search of the EU Intellectual Property Office (EUIPO) and relevant national registries should be conducted to assess the strength of the existing marks and the likelihood of confusion. The attorney can provide a professional opinion on the chances of successfully registering the "Ledger" mark and advise on potential infringement risks.

**Negotiate with Trademark Holder(s):** If, after legal review, the risk of infringement is deemed significant, consider approaching the holder(s) of the earlier trademark(s) for LEDGER. Options could include:

Negotiating a coexistence agreement, outlining specific territories or goods/services where both parties can operate without infringement.
Purchasing or licensing the existing trademark(s).
Failure to address these potential conflicts could result in the EUIPO rejecting the trademark application or the client facing a trademark infringement lawsuit in the future.
